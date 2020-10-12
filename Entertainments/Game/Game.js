new Vue ({
  el: '#app',
  data: {
  events: [],
  Yhealth: 100,
  gameon: false,
  Mhealth: 100,
  Mhealthb: 120,
  },
  methods: {
		attack: function() {
    	var dmg = this.CalDmg(1, 5);
      this.Mhealth -= dmg;

      if (this.CheckWin()) {
      		return;
      }
      this.events.unshift({
      isPlayer: true,
      text: 'You hit the Monster for ' + dmg
      }
      );
      this.Mattack()
    },
    Specialattack: function() {
    	var dmg = this.CalDmg(3, 7);
      this.Mhealth -= dmg;
      if (this.CheckWin()) {
      		return;
      }

      this.events.unshift({
      isPlayer: true,
      text: 'You hit the Monster hard for ' + dmg
      }
      );
      this.Mattack()
    },
    Heal: function() {
    	var max = 300;
      var min = 50;
      var heal = Math.max(Math.floor(Math.random() * max) + 1, min);
      this.Yhealth += heal;

      if (this.Yhealth >= 100) {
				this.Yhealth = 100;
      }
      this.events.unshift({
      isPlayer: true,
      text: 'You Healed ' + heal + ' health'
      }
      );
      this.Mattack()
    },
    Mattack: function() {
      var dmg = this.CalDmg(0, 7);
      this.Yhealth -= dmg;
      this.Mhealth += 1;
      this.CheckWin();
      this.events.unshift({
      isPlayer: false,
      text: 'The Monster hit You for ' + dmg
      }
      );
      if (this.Mhealth > 120) {
				this.Mhealth = 120;
        this.Mhealthb = 100;
      }
    },
    StartGame: function() {
    	this.Yhealth = 100;
      this.Mhealth = 100;
      this.gameon=true;
      this.events=[];
    },
    Endgame: function() {
    	this.gameon=false
      if (confirm('Are You Sure?')) {

      } else this.gameon = true
      return;
    },
    CalDmg: function(min, max) {
    	return Math.max(Math.floor(Math.random() * max) + 1, min);
    },
    CheckWin: function() {
			if (this.Mhealth <= 0) {
    			if (confirm('You Won! Would You Like To Play Again?')) {
    	    	this.StartGame();
    	    }	else {
    	    	this.gameon=false;
    	    }
					return true;
    	} else if (this.Yhealth <= 0) {
      	if (confirm('You Lost! Would You Like To Play Again?')) {
    		    this.StartGame();
    	   }	else {
    	      this.gameon=false;
    	   }
					return true;
      }
          return false;
      }

    }
  })
