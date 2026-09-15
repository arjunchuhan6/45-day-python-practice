"""
Script to add sample notes to the notes application for testing all features.
"""

import json
import os
from datetime import datetime, timedelta

NOTES_FILE = "notes.json"

def add_sample_notes():
    """Add sample notes to demonstrate all features."""
    
    sample_notes = [
        {
            "id": 1,
            "title": "Python Programming Tips",
            "content": "1. Use list comprehensions for efficient loops\n2. Use f-strings for string formatting\n3. Always use virtual environments\n4. Follow PEP 8 style guide\n5. Write unit tests for your code",
            "category": "Programming",
            "created_at": (datetime.now() - timedelta(days=5)).isoformat(),
            "updated_at": (datetime.now() - timedelta(days=5)).isoformat()
        },
        {
            "id": 2,
            "title": "Weekly Shopping List",
            "content": "Milk - 2 liters\nBread - 1 loaf\nEggs - 1 dozen\nChicken - 500g\nRice - 2kg\nOil - 1 liter\nVegetables (tomato, onion, carrot)\nFruit (apple, banana, orange)",
            "category": "Shopping",
            "created_at": (datetime.now() - timedelta(days=3)).isoformat(),
            "updated_at": (datetime.now() - timedelta(days=3)).isoformat()
        },
        {
            "id": 3,
            "title": "Gym Workout Routine",
            "content": "Monday: Chest and Triceps\nTuesday: Back and Biceps\nWednesday: Legs\nThursday: Rest\nFriday: Shoulders and Abs\nSaturday: Cardio\nSunday: Rest\n\nEach session: 5 min warm-up, 45 min workout, 5 min cool-down",
            "category": "Health",
            "created_at": (datetime.now() - timedelta(days=7)).isoformat(),
            "updated_at": (datetime.now() - timedelta(days=7)).isoformat()
        },
        {
            "id": 4,
            "title": "Book Recommendations",
            "content": "1. The Pragmatic Programmer - Dave Thomas\n2. Clean Code - Robert C. Martin\n3. Design Patterns - Gang of Four\n4. Atomic Habits - James Clear\n5. Deep Work - Cal Newport",
            "category": "Books",
            "created_at": (datetime.now() - timedelta(days=2)).isoformat(),
            "updated_at": (datetime.now() - timedelta(days=2)).isoformat()
        },
        {
            "id": 5,
            "title": "JavaScript ES6 Features",
            "content": "Arrow Functions: () => {}\nTemplate Literals: `Hello ${name}`\nDestructuring: const {x, y} = obj\nSpread Operator: ...array\nPromises and async/await\nClasses and inheritance\nModules: import/export",
            "category": "Programming",
            "created_at": (datetime.now() - timedelta(days=4)).isoformat(),
            "updated_at": (datetime.now() - timedelta(days=4)).isoformat()
        },
        {
            "id": 6,
            "title": "Birthday Reminders",
            "content": "Mom - March 15\nDad - July 22\nBest Friend - November 8\nSister - June 10\nCousin - September 5",
            "category": "Personal",
            "created_at": (datetime.now() - timedelta(days=10)).isoformat(),
            "updated_at": (datetime.now() - timedelta(days=10)).isoformat()
        },
        {
            "id": 7,
            "title": "Website Design Ideas",
            "content": "Color Scheme: Blue and white with accent green\nLayout: Modern, minimalist\nFont: Sans-serif (Roboto or Open Sans)\nPages: Home, About, Services, Contact, Blog\nFeatures: Responsive design, dark mode, search functionality\nTechnology Stack: React, Tailwind CSS, Node.js backend",
            "category": "Projects",
            "created_at": (datetime.now() - timedelta(days=1)).isoformat(),
            "updated_at": (datetime.now() - timedelta(days=1)).isoformat()
        },
        {
            "id": 8,
            "title": "Morning Routine",
            "content": "6:00 AM - Wake up\n6:15 AM - Drink water and stretch\n6:30 AM - Meditation (10 mins)\n6:45 AM - Shower\n7:00 AM - Breakfast\n7:30 AM - Read news/emails\n8:00 AM - Start work/study",
            "category": "Personal",
            "created_at": (datetime.now() - timedelta(days=6)).isoformat(),
            "updated_at": (datetime.now() - timedelta(days=6)).isoformat()
        },
        {
            "id": 9,
            "title": "Database Optimization Tips",
            "content": "1. Add appropriate indexes on frequently queried columns\n2. Use EXPLAIN to analyze query performance\n3. Normalize database schema\n4. Implement caching strategies\n5. Batch similar queries together\n6. Use connection pooling\n7. Monitor slow queries regularly",
            "category": "Programming",
            "created_at": (datetime.now() - timedelta(days=8)).isoformat(),
            "updated_at": (datetime.now() - timedelta(days=8)).isoformat()
        },
        {
            "id": 10,
            "title": "Travel Bucket List",
            "content": "- Japan (Tokyo, Kyoto, Mount Fuji)\n- Switzerland (Alps, Zurich)\n- Italy (Rome, Venice, Florence)\n- France (Paris, Provence)\n- Australia (Sydney, Great Barrier Reef)\n- New Zealand (Adventure capital)\n- Iceland (Northern Lights)\n- Canada (Rocky Mountains)",
            "category": "Travel",
            "created_at": (datetime.now() - timedelta(days=9)).isoformat(),
            "updated_at": (datetime.now() - timedelta(days=9)).isoformat()
        }
    ]
    
    # Check if notes.json already exists
    if os.path.exists(NOTES_FILE):
        print(f"[WARNING] '{NOTES_FILE}' already exists. Backing up and creating new one...")
        backup_name = f"{NOTES_FILE}.backup"
        os.rename(NOTES_FILE, backup_name)
        print(f"[OK] Original file backed up to '{backup_name}'")
    
    # Write sample notes to file
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(sample_notes, f, indent=2, ensure_ascii=False)
    
    print(f"\n[OK] Successfully added {len(sample_notes)} sample notes to '{NOTES_FILE}'!")
    print("\n[SAMPLE NOTES CREATED]")
    print("="*80)
    
    for note in sample_notes:
        print(f"ID {note['id']:<2} | {note['title']:<35} | Category: {note['category']:<12}")
    
    print("="*80)
    print("\nYou can now run the application with: python notes_app.py")
    print("\nTry these features:")
    print("  • Search for 'Python' to find programming-related notes")
    print("  • Filter by 'Programming' category to see 3 notes")
    print("  • Filter by 'Personal' category to see 2 notes")
    print("  • Edit any note to test the edit feature")
    print("  • Delete a note to test the delete feature")

if __name__ == "__main__":
    add_sample_notes()
