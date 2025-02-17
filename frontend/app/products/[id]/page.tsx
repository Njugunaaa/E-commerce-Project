"use client";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import axios from "axios";

interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
}

export default function ProductDetailsPage() {
  const { id } = useParams();
  const [product, setProduct] = useState<Product | null>(null);

  useEffect(() => {
    if (id) {
      axios
        .get<Product>(`${process.env.NEXT_PUBLIC_API_URL}/products/${id}/`)
        .then((response) => setProduct(response.data))
        .catch((error) => console.error("Error fetching product:", error));
    }
  }, [id]);

  if (!product) {
    return <p className="text-center text-gray-600">Loading product details...</p>;
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold">{product.name}</h1>
      <p className="text-lg text-gray-700">${product.price}</p>
      <p className="text-gray-500">{product.description}</p>
      <a href="/" className="text-blue-500 underline">Back to Products</a>
    </div>
  );
}
