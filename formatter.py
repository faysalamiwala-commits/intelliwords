# IntelliWords - Book Formatter v1.0
# Made by Faysal Amiwala - Karachi, Pakistan
# Mission: From Idea to Next Reader

def format_book(title, author, chapters):
    print(f"Book: {title}")
    print(f"Author: {author}")
    print(f"Chapters: {len(chapters)}")
    print("="*40)
    for i, ch in enumerate(chapters, 1):
        print(f"\nChapter {i}: {ch}")
        print(f"Formatted for Amazon KDP - Size 6x9 inch")
    print("\nDone! Your book is ready for KDP!")
    print("Made with love by IntelliWords")

# Example
format_book(
    "My First Book", 
    "Faysal Amiwala",
    ["Idea", "Writing", "Publishing", "Earning $2000"]
)
