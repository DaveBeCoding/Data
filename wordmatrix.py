import PyPDF2
from collections import Counter

def parse_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        character_count = 0
        word_count = 0

        # Matrix to store character counts per page
        character_matrix = []

        # Matrix to store words per page
        word_matrix = []

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Count characters and words
            character_count += len(text)
            words = text.split()
            word_count += len(words)

            # Store character counts per page in the matrix
            character_matrix.append(len(text))

            # Store words per page in the matrix
            word_matrix.append(words)

        return character_count, word_count, character_matrix, word_matrix


def display_character_matrix(character_matrix):
    for page_num, character_count in enumerate(character_matrix):
        print(f"Page {page_num + 1}: {character_count} characters")


def display_word_matrix(word_matrix):
    for page_num, words in enumerate(word_matrix):
        print(f"Page {page_num + 1}:")
        word_counts = Counter(words)
        for word, count in word_counts.items():
            print(f"{word}: {count}", end="\t")  # Display word and count with a tab separator
        print()  # Move to the next line


def save_word_matrix_report(word_matrix, file_path):
    with open(file_path, 'w') as file:
        for page_num, words in enumerate(word_matrix):
            file.write(f"Page {page_num + 1}:\n")
            word_counts = Counter(words)
            for word, count in word_counts.items():
                file.write(f"{word}: {count}\t")  # Write word and count with a tab separator
            file.write("\n")  # Move to the next line


if __name__ == "__main__":
    pdf_file = "apple.pdf"  # Replace with your PDF file path
    report_file = "word_matrix_report.txt"

    # Parse the PDF file
    character_count, word_count, character_matrix, word_matrix = parse_pdf(pdf_file)

    # Display results
    print(f"Total Characters: {character_count}")
    print(f"Total Words: {word_count}")
    print("Character Matrix:")
    display_character_matrix(character_matrix)
    print("Word Matrix:")
    display_word_matrix(word_matrix)

    # Save word matrix report to file
    save_word_matrix_report(word_matrix, report_file)
    print(f"Word Matrix report saved to {report_file}")

