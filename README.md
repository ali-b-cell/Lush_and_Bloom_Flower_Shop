elcome to Lush & Bloom, a command-line interface (CLI) application that manages a flower shop's daily operations. This project was built as a Phase 3 assignment using **Python**, **SQLAlchemy**, **Alembic**, and **SQLite**.

Features

- View, add, update, and delete **flowers**, **customers**, and **orders**
- Establish and manage relationships between models:
  - Customers can place multiple orders
  - Each order contains one flower
- Clean and user-friendly CLI menu
- Database migrations using Alembic
- Seed file with realistic data for quick demo setup

Technologies Used

- Python 3.8
- SQLAlchemy (ORM)
- Alembic (migrations)
- SQLite (database)
- Pipenv (environment and dependency management)

 Project Structure

```
lush_and_bloom/
│
├── lib/
│   ├── cli.py               # CLI entry point
│   ├── helpers.py           # CLI helper functions
│   ├── models/
│   │   ├── flower.py        # Flower model
│   │   ├── customer.py      # Customer model
│   │   └── order.py         # Order model
│   ├── db/
│   │   ├── models.py        # SQLAlchemy setup and Base
│   │   └── seed.py          # Seed script
│   ├── migrations/          # Alembic migration folder
│   └── freebies.db          # SQLite database
│
├── alembic.ini              # Alembic config
├── Pipfile / Pipfile.lock   # Pipenv environment files
└── README.md                # Project documentation
```

---

 How to Run the Project

1. **Clone the repository**  
   ```bash
   git clone https://github.com/ali-b-cell/Lush_and_Bloom_Flower_Shope.git
   cd Lush_and_Bloom_Flower_Shope/lush_and_bloom
   ```

2. **Activate the virtual environment**  
   ```bash
   pipenv shell
   ```

3. **Install dependencies**  
   ```bash
   pipenv install
   ```

4. **Run migrations and seed the database**  
   ```bash
   alembic upgrade head
   python lib/db/seed.py
   ```

5. **Start the CLI**  
   ```bash
   python lib/cli.py
   ```

---

 User Experience

- Navigate the CLI menu using numbers and text input
- Real-time feedback for actions like adding/deleting flowers
- Intuitive messages for invalid input and empty records

---

 Example Commands

```bash
# Start CLI
python lib/cli.py

# Re-seed the database
python lib/db/seed.py

# Apply database migrations
alembic upgrade head
```

---

Demo Video

 [Click here to watch the Loom demo](https://www.loom.com/) *(Replace with your Loom link)*

---

 Acknowledgments

Created as a Phase 3 project at **Moringa School**.  
Big thanks to the mentors, peers, and teaching assistants who supported this journey.

---

License

This project is for educational purposes and not licensed for commercial use.




