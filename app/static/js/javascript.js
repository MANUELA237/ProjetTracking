// Sélection des éléments nécessaires
const allDropdown = document.querySelectorAll('#sidebar .side-dropdown');
const sidebar = document.getElementById('sidebar');
const toggleSidebar = document.querySelector('nav .toggle-sidebar');
const allSideDivider = document.querySelectorAll('#sidebar .divider');
const profile = document.querySelector('nav .profile');
const imgProfile = profile.querySelector('img');
const dropdownProfile = profile.querySelector('.profile-link');
const allMenu = document.querySelectorAll('main .content-data .head .menu');
const allProgress = document.querySelectorAll('main .card .progress');

// Fonction pour gérer le toggle de la barre latérale
function toggleSidebarFunction() {
  sidebar.classList.toggle('hide');

  if (sidebar.classList.contains('hide')) {
      allSideDivider.forEach(item => {
          item.textContent = '-';
      });
      allDropdown.forEach(item => {
          const a = item.parentElement.querySelector('a:first-child');
          a.classList.remove('active');
          item.classList.remove('show');
      });
  } else {
      allSideDivider.forEach(item => {
          item.textContent = item.dataset.text;
      });
  }
}

// Événement de clic sur le bouton de toggle de la barre latérale
toggleSidebar.addEventListener('click', toggleSidebarFunction);


// Événement de clic sur le bouton de toggle de la barre latérale
toggleSidebar.addEventListener('click', toggleSidebarFunction);

// Événements pour les dropdowns dans la barre latérale
allDropdown.forEach(item => {
    const a = item.parentElement.querySelector('a:first-child');
    a.addEventListener('click', function (e) {
        e.preventDefault();
        if (!this.classList.contains('active')) {
            allDropdown.forEach(i => {
                const aLink = i.parentElement.querySelector('a:first-child');
                aLink.classList.remove('active');
                i.classList.remove('show');
            });
        }
        this.classList.toggle('active');
        item.classList.toggle('show');
    });
});

// Gestion des événements mouseenter et mouseleave pour la barre latérale
sidebar.addEventListener('mouseleave', function () {
    if (this.classList.contains('hide')) {
        allDropdown.forEach(item => {
            const a = item.parentElement.querySelector('a:first-child');
            a.classList.remove('active');
            item.classList.remove('show');
        });
        allSideDivider.forEach(item => {
            item.textContent = '-';
        });
    }
});

sidebar.addEventListener('mouseenter', function () {
    if (this.classList.contains('hide')) {
        allDropdown.forEach(item => {
            const a = item.parentElement.querySelector('a:first-child');
            a.classList.remove('active');
            item.classList.remove('show');
        });
    }
});

// Événement pour le profil
imgProfile.addEventListener('click', function () {
    dropdownProfile.classList.toggle('show');
});

// Événements pour les menus dans le contenu principal
allMenu.forEach(item => {
    const icon = item.querySelector('.icon');
    const menuLink = item.querySelector('.menu-link');
    icon.addEventListener('click', function () {
        menuLink.classList.toggle('show');
    });
});

// Gestion du clic en dehors des dropdowns
window.addEventListener('click', function (e) {
    if (e.target !== imgProfile && e.target !== dropdownProfile) {
        if (dropdownProfile.classList.contains('show')) {
            dropdownProfile.classList.remove('show');
        }
    }

    allMenu.forEach(item => {
        const icon = item.querySelector('.icon');
        const menuLink = item.querySelector('.menu-link');
        if (e.target !== icon && e.target !== menuLink) {
            if (menuLink.classList.contains('show')) {
                menuLink.classList.remove('show');
            }
        }
    });
});

// Mise à jour des valeurs des barres de progression
allProgress.forEach(item => {
    item.style.setProperty('--value', item.dataset.value);
});



// Gestion du mode sombre
const body = document.querySelector("body");
const modeToggle = document.getElementById("mode-toggle");

modeToggle.addEventListener("click", () => {
    body.classList.toggle("dark");
    if (body.classList.contains(dark)){
      localStorage.setItem("mode","dark");
       }else{
        localStorage.setItem("mode","light");


    }

});

sidebartoggle.addEventListener("clik" , () =>{
  sidebar.classList.toggle("close")

})



