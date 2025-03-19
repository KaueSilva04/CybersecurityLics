// Funcionalidade do botão voltar



document.addEventListener('DOMContentLoaded', () => {


    // Efeito de chuva matrix
    const canvas = document.getElementById('matrix');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    // Caracteres para exibir
    const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+[]{}|;:,.<>?/\\';

    const fontSize = 16;
    const columns = Math.floor(canvas.width / fontSize);

    // Array para rastrear a posição y de cada coluna
    const drops = [];
    for (let i = 0; i < columns; i++) {
        drops[i] = Math.random() * -canvas.height;
    }

    // Função de desenho da chuva matrix
    function draw() {
        // Define um fundo preto semi-transparente para criar efeito de rastro
        ctx.fillStyle = 'rgba(0, 0, 0, 0.09)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Define a cor e fonte para os caracteres
        ctx.fillStyle = '#0f0';
        ctx.font = `${fontSize}px monospace`;

        // Loop através de cada coluna
        for (let i = 0; i < drops.length; i++) {
            // Seleciona um caractere aleatório
            const charIndex = Math.floor(Math.random() * chars.length);
            const text = chars[charIndex];

            // Desenha o caractere
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);

            // Move o caractere para baixo
            drops[i]++;
            // Reinicia se estiver na parte inferior da tela ou aleatoriamente
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.999) {
                drops[i] = 0;
            }

        }
    }

    // Executa a função draw a cada 33ms (aproximadamente 30 FPS)
    setInterval(draw, 45);

    // Alternância de abas
    const tabs = document.querySelectorAll('.tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove a classe ativa de todas as abas e formulários
            document.querySelector('.tab.active').classList.remove('active');
            document.querySelector('.form-container.active').classList.remove('active');

            // Adiciona classe ativa à aba atual e ao formulário correspondente
            tab.classList.add('active');
            document.getElementById(tab.dataset.tab).classList.add('active');
        });
    });

    // Medidor de força da senha
    const passwordInput = document.querySelector('.password-input');
    const strengthBar = document.querySelector('.password-strength span');

    passwordInput?.addEventListener('input', () => {
        const password = passwordInput.value;
        let strength = 0;

        if (password.length > 6) strength += 20;
        if (password.length > 10) strength += 20;
        if (/[A-Z]/.test(password)) strength += 20;
        if (/[0-9]/.test(password)) strength += 20;
        if (/[^A-Za-z0-9]/.test(password)) strength += 20;

        strengthBar.style.width = `${strength}%`;

        if (strength < 40) {
            strengthBar.style.backgroundColor = '#ff3333';
        } else if (strength < 80) {
            strengthBar.style.backgroundColor = '#ffa500';
        } else {
            strengthBar.style.backgroundColor = '#33ff33';
        }
    });

    // Validação de senhas correspondentes
    const confirmPassword = document.getElementById('register-confirm');
    const passwordMatchError = document.getElementById('password-match-error');

    confirmPassword?.addEventListener('input', () => {
        if (confirmPassword.value !== passwordInput.value) {
            passwordMatchError.style.display = 'block';
        } else {
            passwordMatchError.style.display = 'none';
        }
    });

    // Manipuladores de envio de formulário
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    


    // Alternar visibilidade da senha
    function togglePasswordVisibility(inputId, button) {
        const input = document.getElementById(inputId);
        if (input.type === "password") {
            input.type = "text";
            button.textContent = "⚫";
        } else {
            input.type = "password";
            button.textContent = "👁️";
        }
    }



    // Redimensiona o canvas quando o tamanho da janela muda
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
});

