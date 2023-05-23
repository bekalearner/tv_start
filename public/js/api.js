
// ДЛЯ НОВОСТЕЙ

const date = new Date 
const year = date.getFullYear()
const month = (date.getMonth() + 1).toString().padStart(2, '0')
let currentDay = date.getDay();
// const today = [year + "." + month + "." + day].toString()
const week = date.getDay();
const weekDays = ['Md', "Tu", 'Wd', "Th", 'Fr', 'Sat', 'Sun'];
async function getResponce(currentDay){
    const url = `http://127.0.0.1:8000/api/v1/article/list/?page=1&day_of_week=${currentDay}`
    let responce = await fetch(url)
    let content = await responce.json()
   
    
    let news = document.querySelector('.news')
    
    for (let i = 0; i < content.results.length; i++) {
      news.innerHTML += `
      <div class="flex p-2 font-normal text-[1.5em] items-center news_item ">
        <span>
          <p class="font-normal text-[20px]">${content.results[i].time}</p>
          <p class="text-[#BABABA] text-[14px]">MSK</p>
        </span>
        <span class="flex items-center pl-4">
          <p class="text-[15px]"> <span class="text-[#ff1313] font-semibold"></span> ${content.results[i].title}</p>
        </span>
      </div>
      `
      }

    }

addEventListener('DOMContentLoaded', () => {
  // console.log(currentDay);
  getResponce(currentDay);
})














// async function getResponce(data_number){
//   let responce = await fetch(data_number)
//   let content = await responce.json()
//   console.log(content);
//   let news = document.querySelector('.news')
  
//   for (let i = 0; i < content.results.length; i++) {
//     news.innerHTML += `
//     <div class="flex p-2 font-normal text-[1.5em] items-center news_item ">
//       <span>
//         <p class="font-normal text-[20px]">${content.results[i].time}</p>
//         <p class="text-[#BABABA] text-[14px]">MSK</p>
//       </span>
//       <span class="flex items-center pl-4">
//         <p class="text-[15px]"> <span class="text-[#ff1313] font-semibold"></span> ${content.results[i].title}</p>
//       </span>
//     </div>
//     `
//     if(content.results[i].post_date === today){
//         first.textContent = 'Сегодня'
//         data_number = firstUrl
//       }



    // 
    // else if(content.results[i].post_date === today){
    //   second.textContent = 'Сегодня'
    //   data_number = secondUrl
    // }
    // else if(content.results[i].post_date === today){
    //   third.textContent = 'Сегодня'
    //   data_number = thirdUrl
    // }
    // else if(content.results[i].post_date === today){
    //   fourth.textContent = 'Сегодня'
    //   data_number = fourthUrl
    // }
    // else{
    //   console.log('qwerty');
    // }
    

  // }
  // date



// }

// let defaultUrl = "http://127.0.0.1:8000/api/v1/article/list/?page=2"
// getResponce(defaultUrl)

const first = document.querySelector('#first')
const news = document.querySelector('.news')
const firstUrl = first.getAttribute("data-number")
first.addEventListener("click", function(){
  news.innerHTML= "";
  getResponce(1);
})


const second = document.querySelector('#second')
const secondUrl = second.getAttribute("data-number")
second.addEventListener("click", function(){
  news.innerHTML= "";
  getResponce(2);
})


const third = document.querySelector('#third')
const thirdUrl = third.getAttribute("data-number")
third.addEventListener("click", function(){
  news.innerHTML= "";
  getResponce(3);
})

const fourth = document.querySelector('#fourth')
const fourthUrl = fourth.getAttribute("data-number")
fourth.addEventListener("click", function(){
  news.innerHTML= "";
  getResponce(4);
})
const fifth = document.querySelector('#fifth')
const fifthUrl = fifth.getAttribute("data-number")
fifth.addEventListener("click", function(){
  news.innerHTML= "";
  getResponce(5);
})

const sixth = document.querySelector('#sixth')
const sixthUrl = sixth.getAttribute("data-number")
sixth.addEventListener("click", function(){
  news.innerHTML= "";
  getResponce(6);
})

const seventh = document.querySelector('#seventh')
const seventhUrl = seventh.getAttribute("data-number")
seventh.addEventListener("click", function(){
  news.innerHTML= "";
  getResponce(7);
})










// ДЛЯ МАТЧЕЙ




function sendRequest(url, method) {
  if (method === 'GET') {
    let request = fetch(url)
      .then(data => data.json())
    
      return request
  }
}

async function createMatch(parent) {

  const matchList = document.querySelector(parent)

  // console.log(sendRequest('http://127.0.0.1:8000/api/v1/matches/list/', 'GET'))

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


// ДЛЯ КАРТОЧЕК
async function getLive(){
  let responceCard = await fetch('http://127.0.0.1:8000/api/v1/matches/list/')
  let contentCard = await responceCard.json()
  let slicedCard = contentCard.results.slice(0, 6);
  console.log(contentCard);

  let live = document.querySelector('#card_live')
  
  for (let i = 0; i < slicedCard.length; i++){
    live.innerHTML += `
    <div class="border m-auto border-[#ccc] w-[350px] h-[290px] relative">
        <img class="w-full absolute top-0 left-0 " src="${contentCard.results[i].image}" alt="">
        <a class="text-white text-[12px] font-medium hover:underline absolute bottom-[110px] left-[20px]" href="#">${contentCard.results[i].sport_type.name} - ${contentCard.results[i].tournament.name}</a>
        <div class="flex absolute bottom-0 left-0">
          <span class="flex items-center justify-center w-[70px] h-[85px] border-r border-[#ccc]">
            <img class="w-[35px]" src="${contentCard.results[i].sport_type.logo}" alt="">
          </span>
          <span class=" w-[208px] leading-[15px]">
            <p class="text-[12px] text-[#666] pt-[18px] pl-[18px] ">${contentCard.results[i].match_date} / ${contentCard.results[i].time} MSK</p>
            <p class="text-[14px] text-[#BABABA] pl-[18px]">${contentCard.results[i].sport_type.name}. ${contentCard.results[i].tournament.name}. ${contentCard.results[i].tournament.gender}</p> 
          </span>
          <span class="flex items-center justify-center w-[70px] h-[85px]">
            <img class="w-[35px]" src="./public/img/play.png" alt="">
          </span>
        </div>
      </div>
    `
  }
}
getLive()




async function getNards(){
  let responceNards = await fetch('http://127.0.0.1:8000/api/v1/backgammon/list/')
  let contentNards = await responceNards.json()
  let slicedNards = contentNards.results.slice(0, 6);
  console.log(contentNards);

  let nards = document.querySelector('#nards')
  
  for (let i = 0; i < slicedNards.length; i++){
    nards.innerHTML += `
    <div class="border m-auto border-[#ccc] w-[350px] h-[290px] relative">
          <img class="w-full absolute top-0 left-0" src="${contentNards.results[i].image}" alt="">
          <a class="text-white text-[14px] font-medium hover:underline absolute bottom-[110px] left-[20px]" href="#">Нарды. Старт суперлига ${contentNards.results[i].name}</a>
          <div class="flex absolute bottom-0 left-0">
            <span class="flex items-center justify-center w-[70px] h-[85px] border-r border-[#ccc]">
              <img class="w-[35px]" src="./public/img/kub.png" alt="">
            </span>
            <span class="leading-[15px] w-[203px]">
              <p class="text-[12px] text-[#666] pt-[18px] pl-[18px] ">05.12.2022 / 21:45 MSK</p>
              <p class="text-[14px] text-[#BABABA] pl-[18px]">Нарды. СТАРТ Суперлига</p> 
            </span>
            <span class="flex items-center justify-center w-[70px] h-[85px]">
              <img class="w-[35px]" src="./public/img/play.png" alt="">
            </span>
          </div>
        </div>
    `
  }
}
// ${contentCard.results[i].team_one.name}
getNards()