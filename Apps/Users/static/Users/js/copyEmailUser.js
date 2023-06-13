document.addEventListener("DOMContentLoaded", function () {
    // Obtener el botón y el elemento a copiar por su ID
    const btnCopy = document.getElementById("btn-copy-email");
    const elementToCopy = document.getElementById("user_email");

    // Agregar un evento click al botón
    btnCopy.addEventListener("click", function () {
        // Obtener el contenido del elemento a copiar
        const content = elementToCopy.textContent || elementToCopy.innerText;

        // Copiar el contenido al portapapeles
        navigator.clipboard.writeText(content).then(function () {
            // Alerta o mensaje de confirmación (opcional)
            alert("¡Contenido copiado al portapapeles!");
            const originalContent = btnCopy.innerHTML
            btnCopy.classList.add("copied-animation");
            btnCopy.innerHTML = '<svg fill="none" class="w-6 h-6 text-yellow-300" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M11.35 3.836c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m8.9-4.414c.376.023.75.05 1.124.08 1.131.094 1.976 1.057 1.976 2.192V16.5A2.25 2.25 0 0118 18.75h-2.25m-7.5-10.5H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V18.75m-7.5-10.5h6.375c.621 0 1.125.504 1.125 1.125v9.375m-8.25-3l1.5 1.5 3-3.75"></path></svg>'
            setTimeout(function () {
                btnCopy.classList.remove("copied-animation");
                btnCopy.innerHTML = originalContent
            }, 2000)
        }).catch(function (error) {
            console.error("Error al copiar al portapapeles:", error);
        });
    });
});