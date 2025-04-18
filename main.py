from markitdown import MarkItDown


def main():
    """Convert PDF to text and print the content."""
    # Initialize MarkItDown
    markitdown = MarkItDown()

    # Convert PDF to text
    pdf_url = "https://lifull.com/doc/2024/11/20241114_-youshiQA-.pdf"
    result = markitdown.convert(pdf_url)

    # Print the extracted text content
    print(result.text_content)


if __name__ == "__main__":
    main()