const home = document.getElementById("index");
const movie = document.getElementById("movie");
const book = document.getElementById("book");

const IsActive = () => {
  let name = window.location.pathname;
  if (name == "/") {
    home.className = "nav-link active";
    book.className = "nav-link";
    movie.className = "nav-link";
  } else if (name == "/movie") {
    home.className = "nav-link ";
    book.className = "nav-link ";
    movie.className = "nav-link active";
  } else if (name == "/book") {
    home.className = "nav-link ";
    book.className = "nav-link active";
    movie.className = "nav-link ";
  }
};

movie.addEventListener("click", IsActive());
home.addEventListener("click", IsActive());
book.addEventListener("click", IsActive());
