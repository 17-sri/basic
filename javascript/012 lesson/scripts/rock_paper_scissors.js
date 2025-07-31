let score = JSON.parse(localStorage.getItem('score')) || {
      wins : 0,
      loses : 0,
      ties : 0
    };
    updateScoreElement();
    /* this is same as above code
      if (!score) {
        score = {
          wins: 0,
          loses: 0,
          ties: 0
        };
      }
      */

    let isAutoPlay = false;
    let instervalId;

    function autoPlay(){
      if(!isAutoPlay){
        instervalId = setInterval(function(){
          const playerMove = pickComputerMove();
          playGame(playerMove);
        }, 1000);
        isAutoPlay = true;
        
      }else{
        clearInterval(instervalId);
        isAutoPlay = false;
      }  
    }

    function playGame(playerMove) {
      const computerMove = pickComputerMove();
      let result = '';
      if (playerMove === 'rock') {
        if (computerMove === 'rock') {
          result = 'It is a Tie';
        } else if (computerMove === 'paper') {
          result = 'You Lose';
        } else if (computerMove === 'scissors') {
          result = 'You Win'
        }
      }

      else if (playerMove == 'paper') {
        if (computerMove == 'rock') {
          result = 'You Win';
        } else if (computerMove == 'paper') {
          result = 'It is a Tie';
        } else if (computerMove == 'scissors') {
          result = 'You Lose';
        }
      }

      else if (playerMove === 'scissors') {
        if (computerMove == 'rock') {
          result = 'You Lose';
        } else if (computerMove == 'paper') {
          result = 'You Win';
        } else if (computerMove == 'scissors') {
          result = 'It is a Tie';
        }
      }

      if(result ==='You Win'){
        score.wins += 1;
      } else if(result ==='You Lose'){
        score.loses += 1;
      } else if(result ==='It is a Tie'){
        score.ties += 1;
      } 
      localStorage.setItem('score', JSON.stringify(score));
      updateScoreElement();
      document.querySelector('.js-result').innerHTML = result;
      document.querySelector('.js-moves').innerHTML = `you <img src="images/${playerMove}-emoji.png" class="move-icon"><img src="images/${computerMove}-emoji.png" class="move-icon"> computer`;
    }

    function updateScoreElement(){
      document.querySelector('.js-score').innerHTML= `Wins : ${score.wins}, loses : ${score.loses}, Ties : ${score.ties}`;
    }

    function pickComputerMove() {
      const randomNumber = Math.random(); // Used 'const' because it cannot be changed 
      let computerMove = ''; // used 'let' because it can be changed
      if (randomNumber > 0 && randomNumber < 0.33) {
        computerMove = 'rock'
      } else if (randomNumber > 0.33 && randomNumber < 0.66) {
        computerMove = 'paper';
      } else if (randomNumber > 0.66 && randomNumber < 1) {
        computerMove = 'scissors';
      }
      return computerMove;
    }