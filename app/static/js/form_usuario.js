document
  .getElementById("form-usuario")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Impede o envio tradicional do formulário

    // Captura os dados do formulário
    const formData = {
      nome: document.getElementById("username").value,
      senha: document.getElementById("password").value,
    };

    // Envia a requisição AJAX
    fetch("/admin/inserir", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Erro na requisição");
        }
        return response.json();
      })
      .then((data) => {
        const modalBody = document.getElementById("modalBody");
        if (data.success) {
          // Exibe uma mensagem de sucesso no modal
          modalBody.innerHTML = `
            <div class="alert alert-success">${data.message}</div>
            <p>ID: ${data.user.id}</p>
            <p>Nome: ${data.user.nome}</p>
            <p>Senha: ${data.user.senha}</p>
          `;
          // Limpa o formulário
          document.getElementById("form-usuario").reset();
        } else {
          // Exibe uma mensagem de erro no modal
          modalBody.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
        }
        // Abre o modal
        $("#mensagemModal").modal("show");
      })
      .catch((error) => {
        console.error("Erro ao enviar o formulário:", error);
        const modalBody = document.getElementById("modalBody");
        modalBody.innerHTML = `<div class="alert alert-danger">Ocorreu um erro ao processar a requisição.</div>`;
        // Abre o modal
        $("#mensagemModal").modal("show");
      });
  });
