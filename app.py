import streamlit as st
import os

# Define file paths
CHEAT_SHEET_FILE = "kubernetes_cheat_sheet.md"
DOCS_DIR = "docs"

def list_markdown_files(directory):
    """Lists all markdown files in the given directory."""
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if f.endswith(".md")]

def display_markdown_file(filepath):
    """Displays the contents of a Markdown file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            st.markdown(content)
    except Exception as e:
        st.error(f"Error loading {filepath}: {e}")
        
def main():
    st.sidebar.title("Documentation")

    # Get list of Markdown files
    markdown_files = list_markdown_files(DOCS_DIR)

    if not markdown_files:
        st.sidebar.write("No documentation available.")
        return

    # Sidebar navigation for markdown files
    selected_file = st.sidebar.radio("Select a document", markdown_files)

    # Display the selected document
    st.title(selected_file)
    display_markdown_file(os.path.join(DOCS_DIR, selected_file))


if __name__ == "__main__":
    main()
