
import sys

def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    # Check CLI arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get file path from CLI argument
    filepath = sys.argv[1]

    # ✅ Pass filepath to stats.main()
    from stats import main as stats_main
    stats_main(filepath)


if __name__ == "__main__":
    main()


