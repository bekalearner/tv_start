function toggleMenu (){
  const burger = document.querySelector("#burger")
  const menu = document.querySelector("#navbar-default")
  // const body = document.querySelector("body")

  burger.addEventListener('click', () => {
    burger.classList.toggle('active')
    menu.classList.toggle('sm:hidden')
  })
}
toggleMenu()






async function getResponce(){
  let responce = await fetch('http://127.0.0.1:8000/api/v1/article/list/')
  let content = await responce.json()
  console.log(content);

  let news = document.querySelector('.news')


  for (let key in content){
    news.innerHTML += `
    <div class="flex p-2 font-normal text-[1.5em] items-center news_item ">
      <span>
        <p class="font-normal text-[20px]">${content[key].time}</p>
        <p class="text-[#BABABA] text-[14px]">MSK</p>
      </span>
      <span class="flex items-center pl-4">
        <p class="text-[15px]"> <span class="text-[#ff1313] font-semibold"> Прямой Эфир</span> ${content[key].title}</p>
      </span>
    </div>
    `
  }
}
getResponce()














function sendRequest(url, method) {
  if (method === 'GET') {
    let request = fetch(url)
      .then(data => data.json())
    
      return request
  }
}

async function createMatch(parent) {

  const matchList = document.querySelector(parent)

  console.log(sendRequest('http://127.0.0.1:8000/api/v1/matches/list/', 'GET'))

  await sendRequest('http://127.0.0.1:8000/api/v1/matches/list/', 'GET')
    .then(data => {
      data.forEach(title => {
        const match = document.createElement('div')
    
        match.innerHTML = `
            <div class="w-full h-[80px] bg-white flex border border-[#ddd] ">
              <div class="flex items-center justify-center w-[60px] h-[100%] border-r border-[#ddd] ">
                <img class="w-[30px]" src="./public/img/sport_type/sport-volley.png" alt="">
              </div>
              <div class="w-full flex ms:block">
                <div class="w-[15%] h-[100%] flex items-center text-[12px] font-normal text-[#666] pl-2 lg:block ms:w-full ms:h-[28px] ms:flex ms:justify-center">
                  <p class="lg:mt-[19px] ms:mt-0">01.05.2023 / </p>
                  <p > 16:50 MSK</p>
                </div>
                <div class="block w-full">
                  <div class="grid_kiro w-full flex items-center">
                    <div class="flex items-center justify-end font-[600]">
                      <p>${title.team_one.name}</p>
                    </div>
                    <div class="flex items-center justify-center ms:hidden">
                      <img class="w-[40px]" src="./public/img/teams/VC-Sparta.png" alt="">
                    </div>
                    <div class="flex items-center justify-center font-semibold ">
                      <p>--</p>
                    </div>
                    <div class="flex items-center justify-center ms:hidden">
                      <img class="w-[40px]" src="./public/img/teams/Zarechie.png" alt="">
                    </div>
                    <div class="flex items-center  font-[600]">
                      <p>${title.team_two.name}</p>
                    </div>
                  </div>
                  <div class="w-full  ms:hidden">
                    <p class="text-center text-[0.8em] font-normal text-[#BABABA]">${title.sport_type.name} ${title.tournament.name}. ${title.tournament.gender}</p>
                  </div>
                </div>
              </div>
              <div class="flex justify-center items-center w-[60px] h-[100%] border-l border-[#ddd]">
                <img class="w-[30px]" src="./public/img/play.png" alt="">
              </div>
            </div>`
    
            matchList.append(match)
      })
    })
  
}

createMatch('#match')