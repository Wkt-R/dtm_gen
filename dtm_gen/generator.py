import os
from pylibdmtx.pylibdmtx import encode
from PIL import Image

def generate_datamatrix(data, output_path, size=8):
    try:
        encoded = encode(data.encode('utf-8'))
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
        img = img.resize((size * 10, size * 10), Image.Resampling.LANCZOS)
        img.save(output_path)
        print(f"DataMatrix code saved to {output_path}")
        return output_path
    except Exception as e:
        print(f"Error generating DataMatrix: {e}")
        return None

def add_label_to_image(img, text):
    width, height = img.size
    
    new_height = height + 50
    new_img = Image.new('RGB', (width, new_height), color='white')
    
    new_img.paste(img, (0, 0))
    
    draw = ImageDraw.Draw(new_img)
    try:
        font = ImageFont.truetype("Arial", 20)
    except IOError:
        font = ImageFont.load_default()
    
    text_width = draw.textlength(text, font=font)
    if hasattr(draw, 'textlength'):
        text_width = draw.textlength(text, font=font)
    else:
        text_width = font.getlength(text)
    
    draw.text(
        ((width - text_width) // 2, height + 10),
        text,
        fill="black",
        font=font
    )
    
    return new_img

def process_results(results, output_dir, size=8):
    os.makedirs(output_dir, exist_ok=True)
    
    generated_files = []
    
    for i, row in enumerate(results):
        data = str(row[0])
        print(f"Processing item {i+1}: {data}")
        
        safe_data = data.replace(' ', '_').replace('/', '_').replace('\\', '_')
        filename = f"qrcode_{i+1}_{safe_data[:30]}.png"
        image_path = os.path.join(output_dir, filename)
        
        generated_path = generate_datamatrix(data, image_path, size)
        generated_files.append(generated_path)
    
    return generated_files