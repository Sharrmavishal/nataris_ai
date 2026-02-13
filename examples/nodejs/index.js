/**
 * Nataris API - Node.js Example
 * 
 * Install dependencies:
 *   npm install node-fetch
 * 
 * Run:
 *   NATARIS_API_KEY=your_key node index.js
 */

const API_KEY = process.env.NATARIS_API_KEY;
const API_URL = 'https://api.nataris.ai/v1';

if (!API_KEY) {
  console.error('Error: NATARIS_API_KEY environment variable is required');
  console.error('Usage: NATARIS_API_KEY=your_key node index.js');
  process.exit(1);
}

/**
 * Make an inference request
 */
async function inference(prompt, options = {}) {
  const response = await fetch(`${API_URL}/inference`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: options.model || 'qwen2.5-0.5b-instruct-q6_k',
      prompt,
      max_tokens: options.maxTokens || 100,
      temperature: options.temperature || 0.7,
    }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(`API Error: ${error.error?.message || response.statusText}`);
  }

  return response.json();
}

/**
 * List available models
 */
async function listModels() {
  const response = await fetch(`${API_URL}/models`, {
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
    },
  });

  if (!response.ok) {
    throw new Error(`API Error: ${response.statusText}`);
  }

  return response.json();
}

/**
 * Get usage/balance
 */
async function getUsage() {
  const response = await fetch(`${API_URL}/usage`, {
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
    },
  });

  if (!response.ok) {
    throw new Error(`API Error: ${response.statusText}`);
  }

  return response.json();
}

// Main
async function main() {
  console.log('=== Nataris API - Node.js Example ===\n');

  try {
    // 1. Check balance
    console.log('1. Checking balance...');
    const usage = await getUsage();
    console.log(`   Balance: $${usage.balance_usd}`);
    console.log(`   Requests this period: ${usage.total_requests}\n`);

    // 2. List models
    console.log('2. Available models:');
    const models = await listModels();
    models.data.forEach(m => {
      console.log(`   - ${m.id} (${m.type})`);
    });
    console.log('');

    // 3. Make inference
    console.log('3. Making inference request...');
    const result = await inference('Explain AI in one sentence.');
    console.log(`   Model: ${result.model}`);
    console.log(`   Response: ${result.output}`);
    console.log(`   Tokens used: ${result.usage.total_tokens}\n`);

    // 4. Chat Completions (OpenAI-compatible)
    console.log('4. Chat completion...');
    const chatRes = await fetch(`${API_URL}/chat/completions`, {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'llama-3.2-1b-instruct-q4_k_m',
        messages: [{ role: 'user', content: 'What is quantum computing?' }],
        max_tokens: 100,
      }),
    });
    const chat = await chatRes.json();
    console.log(`   Response: ${chat.choices?.[0]?.message?.content?.slice(0, 80)}...\n`);

    // 5. Orchestration — multi-step research workflow
    console.log('5. Orchestrated research workflow...');
    const orchRes = await fetch(`${API_URL}/chat/completions`, {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'llama-3.2-1b-instruct-q4_k_m',
        messages: [{ role: 'user', content: 'Research the impact of AI on healthcare' }],
        orchestration: { enabled: true, workflow: 'research', max_cost_usd: 1.0 },
      }),
    });
    const orch = await orchRes.json();
    console.log(`   Workflow: ${orch.nataris?.workflow_id || 'N/A'}`);
    console.log(`   Steps: ${orch.nataris?.steps_executed || 'N/A'}`);
    console.log(`   Cost: $${orch.nataris?.total_cost_usd || 'N/A'}\n`);

    console.log('=== Done ===');
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

main();
