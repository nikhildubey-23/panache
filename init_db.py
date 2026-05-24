from db import init_tables, seed_admin

if __name__ == '__main__':
    print("Initializing database tables...")
    init_tables()
    print("Tables created successfully.")
    print("Seeding admin user...")
    seed_admin()
    print("Done!")
