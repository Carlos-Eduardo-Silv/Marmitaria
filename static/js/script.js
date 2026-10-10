document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form-pedido");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    const cliente = form.cliente.value.trim();
    const tamanho = form.querySelector('input[name="tamanho"]:checked');

    if (!cliente) {
      e.preventDefault();
      alert("⚠️ Por favor, informe o nome do cliente.");
      form.cliente.focus();
      return;
    }

    if (!tamanho) {
      e.preventDefault();
      alert("⚠️ Por favor, escolha o tamanho da marmita.");
      return;
    }

    alert(`✅ Pedido de ${cliente} (${tamanho.value}) enviado com sucesso!`);
  });

  // Máscara simples: só letras e espaços no nome
  form.cliente.addEventListener("input", (e) => {
    e.target.value = e.target.value.replace(/[^A-Za-zÀ-ÿ\s]/g, "");
  });
});