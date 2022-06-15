document.addEventListener("DOMContentLoaded", function () {
        const fileUploader1 = document.getElementById('file-input-logo');
        const fileUploader2 = document.getElementById('file-input-banner');

        if (fileUploader1) {
            fileUploader1.addEventListener('change', (event) => {
                const logoFiles = event.target.files;
                console.log('files', logoFiles);

                const feedback = document.getElementById('feedback1');
                feedback.innerHTML = `Файл загружен успешно`;
            });
        }
        if (fileUploader2) {
            fileUploader2.addEventListener('change', (event) => {
                const bannerFiles = event.target.files;
                console.log('files', bannerFiles);

                const feedback = document.getElementById('feedback2');
                feedback.innerHTML = `Файл загружен успешно`;
            });
        }
    }
);