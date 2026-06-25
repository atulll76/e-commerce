import asyncio
import os
import sys

# Ensure the project root is in the system path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config.database import AsyncSessionLocal, engine
from app.services import user_service, product_service, order_service

async def main():
    print("==================================================")
    print("    E-COMMERCE SERVICE LAYER VERIFICATION SCRIPT")
    print("==================================================")
    print("[1/2] Verifying module imports...")
    print("[OK] UserService import successful:", user_service)
    print("[OK] ProductService import successful:", product_service)
    print("[OK] OrderService import successful:", order_service)

    print("\n[2/2] Testing service operations with database...")
    try:
        async with AsyncSessionLocal() as session:
            # Query User service
            user = await user_service.get(session, 1)
            if user:
                print(f"[OK] UserService.get(1) success: {user.first_name} {user.last_name}")
            else:
                print("[!] UserService.get(1) returned None")

            # Query Product service
            product = await product_service.get(session, 1)
            if product:
                print(f"[OK] ProductService.get(1) success: {product.product_name}")
            else:
                print("[!] ProductService.get(1) returned None")
                
    except Exception as e:
        print("\n[!] Database service connection failed.")
        print(f"    Error message: {e}")
        
    print("\n==================================================")
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())
