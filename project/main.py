# Import necessary libraries
import os  # Operating system functionalities, used for file path operations
import json  # Library for JSON manipulation
from analyzer import analyze_code, annotate_code  # Import analysis functions from analyzer.py
from analyzer import PlannerAgent  # Import PlannerAgent class from analyzer module
from analyzer import scan_directory_structure  # Import scan_directory_structure function from analyzer module
from analyzer import validate_best_practices  # Import validate_best_practices function from analyzer module
from analyzer import write_detailed_results_to_file  # Import write_detailed_results_to_file function from analyzer module

# Define a function to ensure the 'results' directory exists
def ensure_results_directory():
    """
    Ensure that a 'results' directory exists for storing generated reports.
    """
    results_dir = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    return results_dir

# Define a function to validate if the provided directory path exists
def validate_directory_path(directory_path):
    """
    Validate if the provided directory path exists.

    Args:
        directory_path (str): The directory path to validate.

    Returns:
        bool: True if the directory exists, False otherwise.
    """
    return os.path.isdir(directory_path)

def save_annotated_code(code_content, analysis_results, user_file):
    print("Step 1: Preparing to save the annotated code...")

    # Extract the base name of the user file (without extension)
    base_name = os.path.splitext(os.path.basename(user_file))[0]
    print(f"Step 2: Extracted base name: {base_name}")

    # Define the directory for the annotated file
    annotated_dir = os.path.join(os.getcwd(), f"{base_name}_Annotated")
    print(f"Step 3: Annotated directory path: {annotated_dir}")

    # Create the directory if it doesn't exist
    os.makedirs(annotated_dir, exist_ok=True)
    print(f"Step 4: Created directory (if not existing): {annotated_dir}")

    # Define the path for the annotated code file
    annotated_code_path = os.path.join(annotated_dir, f"{base_name}_annotated.py")
    print(f"Step 5: Annotated code file path: {annotated_code_path}")

    try:
        # Write the annotated code to the file
        with open(annotated_code_path, 'w', encoding='utf-8') as f:
            f.write(annotate_code(code_content, analysis_results))
        print(f"Step 6: Annotated code saved successfully to: {annotated_code_path}")
    except Exception as e:
        print(f"Error: Failed to save annotated code to {annotated_code_path}. Error: {e}")

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
    results_dir = ensure_results_directory()
    json_report_path = os.path.join(results_dir, f"{base_name}_report.json")

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
    print("Starting the annotation process...")
    save_annotated_code(code_content, analysis_results, file_path)
    print("Annotation process completed.")

    # Print a message indicating the completion of the analysis
    print("Analysis complete.")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Analyze Python file")
        print("2. Check file structure best practices")
        print("3. Check folder structure best practices and security vulnerabilities")
        print("4. Plan tool development")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the full path of the Python file to analyze: ")
            if not os.path.isfile(file_path):
                print(f"Error: File '{file_path}' not found.")
                continue
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    code_content = f.read()
                analysis_results = analyze_code(code_content)
                annotated_code_content = annotate_code(code_content, analysis_results)
                results_dir = ensure_results_directory()
                annotated_code_path = os.path.join(results_dir, 'xcode_annotated.py')
                with open(annotated_code_path, 'w', encoding='utf-8') as f:
                    f.write(annotated_code_content)
                print(f"Annotated code saved to: {annotated_code_path}")
            except Exception as e:
                print(f"Error during analysis: {e}")

        elif choice == '2':
            base_path = input("Enter the full path of the directory to analyze: ")
            if not validate_directory_path(base_path):
                print(f"Error: Directory '{base_path}' not found.")
                continue
            directory_structure = scan_directory_structure(base_path)
            validation_results = validate_best_practices(directory_structure)
            results_dir = ensure_results_directory()
            output_file = os.path.join(results_dir, 'analysis_results.txt')
            write_detailed_results_to_file(validation_results, output_file)
            print(f"Detailed results written to {output_file}")

        elif choice == '3':
            base_path = input("Enter the full path of the directory to analyze: ")
            if not validate_directory_path(base_path):
                print(f"Error: Directory '{base_path}' not found.")
                continue
            try:
                directory_structure = scan_directory_structure(base_path)
                results_dir = ensure_results_directory()
                output_file = os.path.join(results_dir, 'folder_structure_analysis.txt')
                with open(output_file, 'w') as f:
                    f.write("Folder Structure Analysis Results:\n\n")
                    f.write("The directory structure was analyzed and categorized as follows:\n")
                    for category, files in directory_structure.items():
                        f.write(f"- {category}: {len(files)} files\n")
                    f.write("\nInsights:\n")
                    f.write("- Ensure that test files are present to validate the codebase effectively.\n")
                    f.write("- Consider organizing data files into a dedicated 'data' folder for better clarity.\n")
                    f.write("- Logs should be rotated or archived periodically to avoid clutter.\n")
                print(f"Folder structure analysis results written to {output_file}")
            except Exception as e:
                print(f"Error during folder structure analysis: {e}")

        elif choice == '4':
            tool_ideas = [
                "Code Smell Detector",
                "Dependency Visualizer",
                "Complexity Analyzer",
                "API Contract Verifier",
                "Dead Code Finder",
                "Git History Insights",
                "License Compliance Checker",
                "Performance Bottleneck Analyzer",
                "Security Vulnerability Scanner",
                "Test Coverage Heatmap",
                "Style Consistency Enforcer",
                "TODO/Comment Tracker",
                "Refactor Suggestion Engine",
                "Build Time Analyzer",
                "Code Duplication Detector",
                "Tech Debt Dashboard",
                "Multi-language Linter Aggregator",
                "Code Comment Quality Checker",
                "Access Control Auditor",
                "Merge Conflict Risk Predictor",
                "Review Readiness Checker",
                "Annotated Architecture Map",
                "Legacy Code Detector",
                "Open Resource Tracker",
                "i18n Audit Tool"
            ]

            planner = PlannerAgent(tool_ideas)
            tasks = planner.decompose_tools()
            dependencies = planner.identify_dependencies()
            prioritized_tasks = planner.prioritize_tasks()

            results_dir = ensure_results_directory()
            output_file = os.path.join(results_dir, 'tool_planning_results.txt')
            with open(output_file, 'w') as f:
                f.write("Tool Planning Results:\n\n")
                f.write("The following tools were decomposed into tasks:\n")
                for task in tasks:
                    f.write(f"- {task['tool']}\n")
                f.write("\nDependencies between tools were identified as follows:\n")
                for tool, deps in dependencies.items():
                    f.write(f"- {tool}: {', '.join(deps) if deps else 'None'}\n")
                f.write("\nThe tools were prioritized in the following order:\n")
                for task in prioritized_tasks:
                    f.write(f"- {task}\n")

            print(f"Tool planning results written to {output_file}")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
