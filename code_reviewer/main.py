# Import necessary libraries
import os  # Operating system functionalities, used for file path operations
import json  # Library for JSON manipulation
from analyzer import analyze_code, annotate_code  # Import analysis functions from analyzer.py

# Define the main function to orchestrate the code review process
def main():
    """Main function to handle user input, file reading, analysis, and output writing."""

    # Prompt the user for the filename
    file_name = input("Please enter the name of the Python file to analyze (must be in the current directory): ")

    # Construct the full path assuming the file is in the current directory
    file_path = os.path.join(os.getcwd(), file_name) # Use current working directory

    # Check if the provided file path exists and is a file
    if not os.path.isfile(file_path):
        # Print an error message if the file doesn't exist
        print(f"Error: File '{file_name}' not found in the current directory ({os.getcwd()}).")
        # Exit the script with a non-zero status code indicating an error
        return

    # Check if the file is a Python file (basic check)
    if not file_path.endswith(".py"):
        # Print an error message if the file is not a .py file
        print(f"Error: Provided file '{file_path}' is not a Python (.py) file.")
        # Exit the script
        return

    # Print a message indicating the start of the analysis
    print(f"Analyzing file: {file_path}...")

    # Read the content of the target Python file
    try:
        # Open the file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as f:
            # Read the entire content of the file
            code_content = f.read()
    except Exception as e:
        # Print an error message if reading the file fails
        print(f"Error reading file {file_path}: {e}")
        # Exit the script
        return

    # Perform the code analysis using the imported function
    try:
        analysis_results = analyze_code(code_content)
    except Exception as e:
        print(f"Error during code analysis: {e}")
        return

    # --- Generate JSON Report --- 
    # Get the base name of the file (e.g., 'sample_code' from 'sample_code.py')
    base_name = os.path.splitext(file_name)[0] # Use file_name instead of os.path.basename(file_path)
    # Define the path for the JSON output file
    json_report_path = f"{base_name}_report.json"

    # Structure the final JSON report according to the README format
    report_data = {
        "file_name": file_name, # Use file_name instead of os.path.basename(file_path)
        "analysis_summary": [] # Initialize the list for rule summaries
    }
    # Iterate through the analysis results (violations grouped by rule ID)
    for rule_id, result in analysis_results.items():
        # Append each rule's violations to the summary list
        report_data["analysis_summary"].append({
            "rule_id": rule_id,
            "violations": result.get("violations", []) # Get violations or empty list
        })

    # Write the JSON report to the file
    try:
        # Open the report file in write mode with UTF-8 encoding
        with open(json_report_path, 'w', encoding='utf-8') as f:
            # Dump the report data into the file with indentation for readability
            json.dump(report_data, f, indent=4)
        # Print confirmation message for the JSON report
        print(f"JSON report saved to: {json_report_path}")
    except Exception as e:
        # Print an error message if writing the JSON report fails
        print(f"Error writing JSON report {json_report_path}: {e}")

    # --- Generate Annotated Code --- 
    # Create the annotated code using the imported function
    annotated_code_content = annotate_code(code_content, analysis_results)
    # Define the path for the annotated code file
    annotated_code_path = f"{base_name}_annotated.py"

    # Write the annotated code to the file
    try:
        # Open the annotated code file in write mode with UTF-8 encoding
        with open(annotated_code_path, 'w', encoding='utf-8') as f:
            # Write the annotated code content to the file
            f.write(annotated_code_content)
        # Print confirmation message for the annotated code file
        print(f"Annotated code saved to: {annotated_code_path}")
    except Exception as e:
        # Print an error message if writing the annotated code fails
        print(f"Error writing annotated code {annotated_code_path}: {e}")

    # Print a message indicating the completion of the analysis
    print("Analysis complete.")

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    # Call the main function to start the process
    main()
