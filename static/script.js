window.addEventListener('scroll', function() {
  let elements = document.querySelectorAll('#num1[data-val]');

  elements.forEach(function(element) {
    // Sayfanın her 1/4'ünde bir animasyonu başlat
    if (element.getBoundingClientRect().top < window.innerHeight / 1) {
      if (!element.hasAttribute('data-animated')) {
        element.setAttribute('data-animated', 'true');

        let start = 0; // Başlangıç değeri
        let end = parseInt(element.getAttribute('data-val')); // Hedef değer
        let duration = 2000; // Animasyon süresi (milisaniye)

        let range = end - start;
        let current = start;
        let increment = end > start ? 40 : 40;
        let stepTime = Math.abs(Math.floor(duration / range));

        // Sayıyı güncellemek için interval
        let timer = setInterval(function() {
          current += increment;
          element.textContent = current;

          if (current == end) {
            clearInterval(timer);
          }
        }, stepTime);
      }
    }
  });
});


// 2


window.addEventListener('scroll', function() {
  let elements = document.querySelectorAll('#num2[data-val]');

  elements.forEach(function(element) {
    // Sayfanın her 1/4'ünde bir animasyonu başlat
    if (element.getBoundingClientRect().top < window.innerHeight / 1) {
      if (!element.hasAttribute('data-animated')) {
        element.setAttribute('data-animated', 'true');

        let start = 0; // Başlangıç değeri
        let end = parseInt(element.getAttribute('data-val')); // Hedef değer
        let duration = 2000; // Animasyon süresi (milisaniye)

        let range = end - start;
        let current = start;
        let increment = end > start ? 40 : 40;
        let stepTime = Math.abs(Math.floor(duration / range));

        // Sayıyı güncellemek için interval
        let timer = setInterval(function() {
          current += increment;
          element.textContent = current;

          if (current == end) {
            clearInterval(timer);
          }
        }, stepTime);
      }
    }
  });
});

window.addEventListener('scroll', function() {
  let elements = document.querySelectorAll('#num3[data-val]');

  elements.forEach(function(element) {
    // Sayfanın her 1/4'ünde bir animasyonu başlat
    if (element.getBoundingClientRect().top < window.innerHeight / 1) {
      if (!element.hasAttribute('data-animated')) {
        element.setAttribute('data-animated', 'true');

        let start = 0; // Başlangıç değeri
        let end = parseInt(element.getAttribute('data-val')); // Hedef değer
        let duration = 2000; // Animasyon süresi (milisaniye)

        let range = end - start;
        let current = start;
        let increment = end > start ? 40 : 40;
        let stepTime = Math.abs(Math.floor(duration / range));

        // Sayıyı güncellemek için interval
        let timer = setInterval(function() {
          current += increment;
          element.textContent = current;

          if (current == end) {
            clearInterval(timer);
          }
        }, stepTime);
      }
    }
  });
});


window.addEventListener('scroll', function() {
  let elements = document.querySelectorAll('#num4[data-val]');

  elements.forEach(function(element) {
    // Sayfanın her 1/4'ünde bir animasyonu başlat
    if (element.getBoundingClientRect().top < window.innerHeight / 1) {
      if (!element.hasAttribute('data-animated')) {
        element.setAttribute('data-animated', 'true');

        let start = 0; // Başlangıç değeri
        let end = parseInt(element.getAttribute('data-val')); // Hedef değer
        let duration = 2000; // Animasyon süresi (milisaniye)

        let range = end - start;
        let current = start;
        let increment = end > start ? 40 : 40;
        let stepTime = Math.abs(Math.floor(duration / range));

        // Sayıyı güncellemek için interval
        let timer = setInterval(function() {
          current += increment;
          element.textContent = current;

          if (current == end) {
            clearInterval(timer);
          }
        }, stepTime);
      }
    }
  });
});

window.addEventListener('scroll', function() {
  let elements = document.querySelectorAll('#num5[data-val]');

  elements.forEach(function(element) {
    // Sayfanın her 1/4'ünde bir animasyonu başlat
    if (element.getBoundingClientRect().top < window.innerHeight / 1) {
      if (!element.hasAttribute('data-animated')) {
        element.setAttribute('data-animated', 'true');

        let start = 0; // Başlangıç değeri
        let end = parseInt(element.getAttribute('data-val')); // Hedef değer
        let duration = 2000; // Animasyon süresi (milisaniye)

        let range = end - start;
        let current = start;
        let increment = end > start ? 40 : 40;
        let stepTime = Math.abs(Math.floor(duration / range));

        // Sayıyı güncellemek için interval
        let timer = setInterval(function() {
          current += increment;
          element.textContent = current;

          if (current == end) {
            clearInterval(timer);
          }
        }, stepTime);
      }
    }
  });
});

window.addEventListener('scroll', function() {
  let elements = document.querySelectorAll('#num6[data-val]');

  elements.forEach(function(element) {
    // Sayfanın her 1/4'ünde bir animasyonu başlat
    if (element.getBoundingClientRect().top < window.innerHeight / 1) {
      if (!element.hasAttribute('data-animated')) {
        element.setAttribute('data-animated', 'true');

        let start = 0; // Başlangıç değeri
        let end = parseInt(element.getAttribute('data-val')); // Hedef değer
        let duration = 2000; // Animasyon süresi (milisaniye)

        let range = end - start;
        let current = start;
        let increment = end > start ? 40 : 40;
        let stepTime = Math.abs(Math.floor(duration / range));

        // Sayıyı güncellemek için interval
        let timer = setInterval(function() {
          current += increment;
          element.textContent = current;

          if (current == end) {
            clearInterval(timer);
          }
        }, stepTime);
      }
    }
  });
});
function hideEmptyCartMessageAndButton() {
  const emptyCartMessage = document.getElementById('empty-cart-message');
  const goToCoursesButton = document.getElementById('go-to-courses');

  if (emptyCartMessage && goToCoursesButton) {
      emptyCartMessage.style.display = 'none';
      goToCoursesButton.style.display = 'none';
  }
}

function showEmptyCartMessageAndButton() {
  const emptyCartMessage = document.getElementById('empty-cart-message');
  const goToCoursesButton = document.getElementById('go-to-courses');
  const cartContainer = document.querySelector('.cart-container');

  if (emptyCartMessage && goToCoursesButton && cartContainer) {
      emptyCartMessage.style.display = 'block';
      goToCoursesButton.style.display = 'block';
      cartContainer.style.height = '100vh';
  }
}

function updateCartVisibility() {
  const cartItems = document.getElementById('cart-items');
  const productsDiv = document.getElementById('products-div');
  const paymentsDiv = document.getElementById('payments-div');

  if (cartItems && productsDiv && paymentsDiv) {
      if (cartItems.children.length > 0) {
          hideEmptyCartMessageAndButton();
          paymentsDiv.style.display = 'block';
      } else {
          showEmptyCartMessageAndButton();
          productsDiv.style.margin = 'auto';
          paymentsDiv.style.display = 'none';
          cartItems.style.backgroundColor = 'transparent';
      }
  }
}

function confirmDelete(productId) {
  const userConfirmed = confirm('Ürünü sepetten silmek istediğinize emin misiniz?');

  if (userConfirmed) {
      const productElement = document.getElementById(productId);
      if (productElement) {
          productElement.remove();
          alert('Ürün başarıyla sepetten silindi');
          updateCartVisibility();
      }
  }
}

window.onload = function () {
  updateCartVisibility();
}

window.addEventListener('scroll', function () {
  const navbar = document.querySelector('nav');
  if (window.scrollY > 0) {
    navbar.classList.remove('bg-gradient-to-t', 'from-lacivert', 'via-mavi', 'to-mor');
    navbar.classList.add('bg-gradient-to-r', 'from-lacivert', 'via-mavi', 'to-mor');
    navbar.classList.add('fixed', 'top-0', 'left-0', 'w-full', 'z-10'); // Navbar'ı sabitleyin
  } else {
    navbar.classList.add('bg-gradient-to-t', 'from-lacivert', 'via-mavi', 'to-mor');
    navbar.classList.remove('bg-gradient-to-r','fixed', 'top-0', 'left-0', 'w-full', 'z-10'); // Navbar'ı çözün
  }
});

document.addEventListener("DOMContentLoaded", function() {
  const searchIcon = document.getElementById("search-icon");
  const searchBar = document.getElementById("search-bar");

  searchIcon.addEventListener("click", function() {
      if (searchBar.classList.contains("hidden")) {
          searchBar.classList.remove("hidden");
      } else {
          searchBar.classList.add("hidden");
      }
  });
});

const searchIcon = document.querySelector('.fa-search');
const searchForm = document.querySelector('#search-form');

searchIcon.addEventListener('click', function() {
  searchForm.classList.toggle('hidden');
});

function toggleLanguageDropdown() {
  var dropdown = document.getElementById("language-dropdown-menu");
  if (dropdown.style.display === "block") {
    dropdown.style.display = "none";
} else {
    dropdown.style.display = "block";
}
};
  // dropdown.classList.toggle("hidden");


function toggleMobileMenu() {
  var mobileMenu = document.getElementById("navbar-language");

  if (mobileMenu.style.display === "block") {
    mobileMenu.style.display = "none";
} else {
    mobileMenu.style.display = "block";
}
};
  // mobileMenu.classList.toggle("hidden");

var languageDropdownToggle = document.querySelector("[data-dropdown-toggle=language-dropdown-menu]");
languageDropdownToggle.addEventListener("click", toggleLanguageDropdown);

var mobileMenuToggle = document.querySelector("[data-collapse-toggle=navbar-language]");
mobileMenuToggle.addEventListener("click", toggleMobileMenu);


var fname = document.getElementById("fname");
var userMenu = document.getElementById("userMenu");

fname.addEventListener("click", function () {
    if (userMenu.style.display === "none" || userMenu.style.display === "") {
        userMenu.style.display = "block";
    } else {
        userMenu.style.display = "none";
    }
});


// carousel 

function setupCarousel(carouselIndex) {
    const carousel = document.querySelectorAll('.carousel')[carouselIndex];
    const slides = carousel.querySelectorAll('.carousel__slide');
    let currentIndex = 0;
  
    function showSlide(index) {
      slides.forEach((slide, i) => {
        slide.style.display = i === index ? 'block' : 'none';
      });
    }
  
    showSlide(currentIndex);
  
    const prevButton = carousel.querySelector('.carousel__arrow--left');
    const nextButton = carousel.querySelector('.carousel__arrow--right');
  
    prevButton.addEventListener('click', () => {
      currentIndex = (currentIndex - 1 + slides.length) % slides.length;
      showSlide(currentIndex);
    });
  
    nextButton.addEventListener('click', () => {
      currentIndex = (currentIndex + 1) % slides.length;
      showSlide(currentIndex);
    });
  }  
  for (let i = 0; i < 6; i++) {
    setupCarousel(i);
  }



  