import json
import os
from datetime import datetime
from pathlib import Path

NOTES_FILE = "notes.json"

def load_notes():
    """Load notes from the JSON file."""
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_notes(notes):
    """Save notes to the JSON file."""
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)

def create_note(title, content, category="General"):
    """Create a new note."""
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "category": category,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)
    print(f"\n✓ Note created successfully! (ID: {note['id']})")
    return note

def view_all_notes():
    """Display all notes."""
    notes = load_notes()
    if not notes:
        print("\n✗ No notes found. Create a note first!\n")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<5} {'Title':<30} {'Category':<15} {'Created':<20}")
    print("="*80)
    
    for note in notes:
        created = datetime.fromisoformat(note['created_at']).strftime("%Y-%m-%d %H:%M")
        print(f"{note['id']:<5} {note['title']:<30} {note['category']:<15} {created:<20}")
    
    print("="*80 + "\n")

def view_note(note_id):
    """View a specific note by ID."""
    notes = load_notes()
    note = next((n for n in notes if n['id'] == note_id), None)
    
    if not note:
        print(f"\n✗ Note with ID {note_id} not found.\n")
        return
    
    print("\n" + "="*80)
    print(f"ID: {note['id']} | Category: {note['category']}")
    print(f"Title: {note['title']}")
    print(f"Created: {datetime.fromisoformat(note['created_at']).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Updated: {datetime.fromisoformat(note['updated_at']).strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*80)
    print(note['content'])
    print("="*80 + "\n")

def edit_note(note_id, new_title=None, new_content=None, new_category=None):
    """Edit an existing note."""
    notes = load_notes()
    note = next((n for n in notes if n['id'] == note_id), None)
    
    if not note:
        print(f"\n✗ Note with ID {note_id} not found.\n")
        return
    
    if new_title:
        note['title'] = new_title
    if new_content:
        note['content'] = new_content
    if new_category:
        note['category'] = new_category
    
    note['updated_at'] = datetime.now().isoformat()
    save_notes(notes)
    print(f"\n✓ Note {note_id} updated successfully!\n")

def delete_note(note_id):
    """Delete a note by ID."""
    notes = load_notes()
    original_count = len(notes)
    notes = [n for n in notes if n['id'] != note_id]
    
    if len(notes) == original_count:
        print(f"\n✗ Note with ID {note_id} not found.\n")
        return
    
    save_notes(notes)
    print(f"\n✓ Note {note_id} deleted successfully!\n")

def search_notes(keyword):
    """Search notes by title or content."""
    notes = load_notes()
    keyword_lower = keyword.lower()
    
    results = [n for n in notes if keyword_lower in n['title'].lower() or keyword_lower in n['content'].lower()]
    
    if not results:
        print(f"\n✗ No notes found matching '{keyword}'.\n")
        return
    
    print(f"\n✓ Found {len(results)} note(s) matching '{keyword}':")
    print("="*80)
    print(f"{'ID':<5} {'Title':<30} {'Category':<15} {'Created':<20}")
    print("="*80)
    
    for note in results:
        created = datetime.fromisoformat(note['created_at']).strftime("%Y-%m-%d %H:%M")
        print(f"{note['id']:<5} {note['title']:<30} {note['category']:<15} {created:<20}")
    
    print("="*80 + "\n")

def view_by_category(category):
    """View all notes in a specific category."""
    notes = load_notes()
    filtered = [n for n in notes if n['category'].lower() == category.lower()]
    
    if not filtered:
        print(f"\n✗ No notes found in category '{category}'.\n")
        return
    
    print(f"\n✓ Notes in category '{category}':")
    print("="*80)
    print(f"{'ID':<5} {'Title':<30} {'Created':<20}")
    print("="*80)
    
    for note in filtered:
        created = datetime.fromisoformat(note['created_at']).strftime("%Y-%m-%d %H:%M")
        print(f"{note['id']:<5} {note['title']:<30} {created:<20}")
    
    print("="*80 + "\n")

def show_menu():
    """Display the main menu."""
    print("\n" + "="*80)
    print("📝 NOTES APPLICATION")
    print("="*80)
    print("1. Create a new note")
    print("2. View all notes")
    print("3. View a specific note")
    print("4. Edit a note")
    print("5. Delete a note")
    print("6. Search notes")
    print("7. View notes by category")
    print("8. Exit")
    print("="*80 + "\n")

def main():
    """Main application loop."""
    while True:
        show_menu()
        choice = input("Select an option (1-8): ").strip()
        
        if choice == '1':
            title = input("\nEnter note title: ").strip()
            if not title:
                print("✗ Title cannot be empty!")
                continue
            
            content = input("Enter note content: ").strip()
            if not content:
                print("✗ Content cannot be empty!")
                continue
            
            category = input("Enter category (default: General): ").strip() or "General"
            create_note(title, content, category)
        
        elif choice == '2':
            view_all_notes()
        
        elif choice == '3':
            view_all_notes()
            try:
                note_id = int(input("Enter note ID to view: ").strip())
                view_note(note_id)
            except ValueError:
                print("\n✗ Please enter a valid number.\n")
        
        elif choice == '4':
            view_all_notes()
            try:
                note_id = int(input("Enter note ID to edit: ").strip())
                notes = load_notes()
                if not any(n['id'] == note_id for n in notes):
                    print(f"\n✗ Note with ID {note_id} not found.\n")
                    continue
                
                print("\nLeave blank to keep current value:")
                new_title = input("New title: ").strip() or None
                new_content = input("New content: ").strip() or None
                new_category = input("New category: ").strip() or None
                
                edit_note(note_id, new_title, new_content, new_category)
            except ValueError:
                print("\n✗ Please enter a valid number.\n")
        
        elif choice == '5':
            view_all_notes()
            try:
                note_id = int(input("Enter note ID to delete: ").strip())
                confirm = input(f"Are you sure you want to delete note {note_id}? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    delete_note(note_id)
                else:
                    print("\n✗ Deletion cancelled.\n")
            except ValueError:
                print("\n✗ Please enter a valid number.\n")
        
        elif choice == '6':
            keyword = input("\nEnter search keyword: ").strip()
            if not keyword:
                print("✗ Keyword cannot be empty!")
                continue
            search_notes(keyword)
        
        elif choice == '7':
            category = input("\nEnter category name: ").strip()
            if not category:
                print("✗ Category cannot be empty!")
                continue
            view_by_category(category)
        
        elif choice == '8':
            print("\n👋 Thank you for using Notes Application. Goodbye!\n")
            break
        
        else:
            print("\n✗ Invalid option. Please select a number between 1 and 8.\n")

if __name__ == "__main__":
    main()
