import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate DataMatrix images from input data")
    
    """
    parser.add_argument("--host", default="localhost", help="Database host")
    parser.add_argument("--port", default="5432", help="Database port")
    parser.add_argument("--dbname", help="Database name")
    parser.add_argument("--user", help="Database user")
    parser.add_argument("--password", help="Database password")
    parser.add_argument("--table", help="Table name")
    parser.add_argument("--column", help="Column containing data for DataMatrix")
    parser.add_argument("--condition", help="WHERE condition (e.g., 'id=123')")
    """
    
    parser.add_argument("--input", required=True, 
                        help="Input string of 11 numbers to encode (e.g., '12345678912')")
    
    parser.add_argument("--output-dir", default="./datamatrix_outputs", 
                        help="Directory to save DataMatrix images")
    parser.add_argument("--size", type=int, default=8, help="DataMatrix size (default: 8)")
    
    return parser.parse_args()