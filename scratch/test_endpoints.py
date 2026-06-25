import os
import sys

# Ensure the project root is in the system path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

def test_routes():
    print("Listing FastAPI app routes:")
    all_paths = []
    for route in app.routes:
        if hasattr(route, "path"):
            print(f"Route Path: {route.path} | Name: {route.name}")
            all_paths.append(route.path)
        elif hasattr(route, "original_router") and hasattr(route.original_router, "routes"):
            print(f"Included Router: {route.original_router.prefix or '/'}")
            for subroute in route.original_router.routes:
                full_path = subroute.path
                print(f"  Subroute Path: {full_path} | Name: {subroute.name}")
                all_paths.append(full_path)

    # Asserts
    assert "/verify/users/{user_id}" in all_paths, "Verification user route missing"
    assert "/users" in all_paths, "Users list route missing"
    assert "/products" in all_paths, "Products list route missing"
    assert "/orders" in all_paths, "Orders list route missing"
    
    print("\n[OK] All CRUD routers successfully verified and registered in FastAPI application!")

if __name__ == "__main__":
    test_routes()
