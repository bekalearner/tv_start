function toggleMenu (){
  const burger = document.querySelector("#burger")
  const menu = document.querySelector("#navbar-default")
  // const body = document.querySelector("body")

  burger.addEventListener('click', () => {
    burger.classList.toggle('active')
    menu.classList.toggle('hidden')
    menu.classList.toggle('flex')
  })
}
toggleMenu()