import asyncio
import os
import sys

# Ensure the project root is in the system path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import select
from app.config.database import AsyncSessionLocal, engine
from app.models.user import User
from app.models.product import Product
from app.repositories.user_repository import user_repository
from app.repositories.product_repository import product_repository
from app.repositories.order_repository import order_repository

async def main():
    print("==================================================")
    print("    E-COMMERCE REPOSITORY VERIFICATION SCRIPT")
    print("==================================================")
    print("[1/2] Verifying module imports and schema mapping...")
    
    # Verify mapping metadata compilation
    print("[OK] Successfully loaded declarative mappings:")
    print(f"  - User base table key: '{user_repository.pk_name}'")
    print(f"  - Product base table key: '{product_repository.pk_name}'")
    print(f"  - Orders base table key: '{order_repository.pk_name}'")
    
    print("\n[2/2] Connecting to database...")
    try:
        async with AsyncSessionLocal() as session:
            # Query User schema
            user_stmt = select(User).limit(5)
            user_res = await session.execute(user_stmt)
            users = user_res.scalars().all()
            
            print("[OK] Connection successful!")
            print(f"\nFound {len(users)} users in database:")
            for user in users:
                print(f"  - ID: {user.user_id} | Name: {user.first_name} {user.last_name} ({user.email})")

            # Query Product schema
            prod_stmt = select(Product).limit(5)
            prod_res = await session.execute(prod_stmt)
            products = prod_res.scalars().all()
            
            print(f"\nFound {len(products)} products in database:")
            for prod in products:
                print(f"  - ID: {prod.product_id} | {prod.product_name} | Price: {prod.price} | Stock: {prod.stock_quantity}")
                
    except Exception as e:
        print("\n[!] Database connection failed.")
        print(f"    Error message: {e}")
        print("\n    Note: Source imports and SQLAlchemy mappings compiled cleanly.")
        print("    If testing execution, ensure MySQL is running locally at port 3306")
        print("    with database 'e_commerce' and credentials 'root' / 'Atul@123'.")
        
    print("\n==================================================")
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())
