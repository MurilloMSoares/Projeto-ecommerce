// Abre e fecha o menu mobile e mantém o atributo de acessibilidade atualizado.
const botaoMenu = document.querySelector(".menu-toggle");
const navegacao = document.querySelector("#menu-principal");

if (botaoMenu && navegacao) {
    botaoMenu.addEventListener("click", () => {
        const estaAberto = botaoMenu.getAttribute("aria-expanded") === "true";

        botaoMenu.setAttribute("aria-expanded", String(!estaAberto));
        botaoMenu.setAttribute(
            "aria-label",
            estaAberto ? "Abrir menu" : "Fechar menu"
        );

        navegacao.classList.toggle("aberto", !estaAberto);
    });

    // Ao escolher uma seção, o menu fecha para não cobrir o conteúdo.
    navegacao.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            botaoMenu.setAttribute("aria-expanded", "false");
            botaoMenu.setAttribute("aria-label", "Abrir menu");
            navegacao.classList.remove("aberto");
        });
    });

    // Se a janela passar para o layout de PC, removemos o estado mobile.
    window.addEventListener("resize", () => {
        if (window.innerWidth > 700) {
            botaoMenu.setAttribute("aria-expanded", "false");
            botaoMenu.setAttribute("aria-label", "Abrir menu");
            navegacao.classList.remove("aberto");
        }
    });
}
