"use client";
import { useEffect, useState } from "react";
import axios from "axios";

// ✅ Define the product type
interface Product {
  id: number;
  name: string;
  price: number;
}

export default function ProductsPage() {
  // ✅ Use the defined type in state
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    axios
      .get<Product[]>(`${process.env.NEXT_PUBLIC_API_URL}/products/`)
      .then((response) => setProducts(response.data))
      .catch((error) => console.error("Error fetching products:", error));
  }, []);

  return (
    <div className="container mx-auto">
      <h1 className="text-2xl font-bold text-center my-4">Products</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {products.length > 0 ? (
          products.map((product) => (
            <div key={product.id} className="border p-4 rounded-lg shadow-md">
              <h2 className="text-lg font-semibold">{product.name}</h2>
              <p className="text-gray-500">${product.price}</p>
              <a
                href={`/products/${product.id}`}
                className="text-blue-500 underline"
              >
                View Details
              </a>
            </div>
          ))
        ) : (
          <p className="text-center text-gray-600">No products found.</p>
        )}
      </div>
    </div>
  );
}
