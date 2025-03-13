from dtm_gen import generator
from dtm_gen import cli
from dtm_gen import processor

def main():
    args = cli.parse_arguments()
    
    try:
        input_data = args.input
        processed_data = processor.process_input_string(input_data)
        print(f"Input data: {input_data}")
        print(f"Processed data: {processed_data}")
        
        results = [(processed_data,)]
        
        generated_files = generator.process_results(results, args.output_dir, args.size)
        
        print(f"Process completed. DataMatrix image generated in {args.output_dir}")
        
    except ValueError as e:
        print(f"Error processing input: {e}")
    
    """
    # Database connection code (commented out for now)
    conn = db.connect_to_database(
        args.host, 
        args.port, 
        args.dbname, 
        args.user, 
        args.password
    )
    
    # Get data from table
    results = db.get_data_from_table(conn, args.table, args.column, args.condition)
    
    if not results:
        print("No data retrieved from database.")
        conn.close()
        return
    
    print(f"Retrieved {len(results)} rows from database.")
    
    # Process results and generate DataMatrix images
    generated_files = generator.process_results(results, args.output_dir, args.size)
    
    # Close database connection
    conn.close()
    """

if __name__ == "__main__":
    main()