// === AGIengineX Worker ===

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // === Token-based Auth ===
    const authHeader = request.headers.get("Authorization");
    const validToken = env.API_TOKEN; // You will set this in Cloudflare

    if (!authHeader || authHeader !== `Bearer ${validToken}`) {
      return new Response("Unauthorized", { status: 401 });
    }

    // === Routes ===

    // Health check
    if (url.pathname === "/agi") {
      return new Response(JSON.stringify({
        success: true,
        agent: "AGIengineX",
        message: "AGIaaS API is LIVE 🚀",
        timestamp: Date.now()
      }), { status: 200, headers: { "Content-Type": "application/json" } });
    }

    // Proxy to Python API
    const backendURL = "https://YOUR-PYTHON-API-URL"; // Example: https://agienginex-render.onrender.com

    const targetURL = backendURL + url.pathname + url.search;

    const backendResponse = await fetch(targetURL, {
      method: request.method,
      headers: request.headers,
      body: request.body
    });

    return backendResponse;
  }
};
