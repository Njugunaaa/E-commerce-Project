import { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  env: {
    NEXT_PUBLIC_API_URL: "http://127.0.0.1:8000/api", // Backend URL
  },
};

export default nextConfig;
