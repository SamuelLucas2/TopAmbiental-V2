document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.getElementById('menu-btn');
    const sidebar = document.getElementById('sidebar');

    if (menuBtn && sidebar) {
        menuBtn.addEventListener('click', function(event) {
            event.stopPropagation();
            sidebar.classList.toggle('active');
            document.body.classList.toggle('sidebar-open');
        });

        document.addEventListener('click', function(event) {
            const isClickInsideSidebar = sidebar.contains(event.target);
            const isClickOnMenuBtn = menuBtn.contains(event.target);

            if (!isClickInsideSidebar && !isClickOnMenuBtn && sidebar.classList.contains('active')) {
                sidebar.classList.remove('active');
                document.body.classList.remove('sidebar-open');
            }
        });
    }
});