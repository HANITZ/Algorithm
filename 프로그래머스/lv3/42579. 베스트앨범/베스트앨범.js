function solution(genres, plays) {
  const play = {};
  const genre = {};
  const music = {};
  const checkGenre = {};
  var answer = [];
  for (let i = 0; i < genres.length; i++) {
    var gen = genres[i];
    play[gen] = play[gen] ? play[gen] + plays[i] : plays[i];
    checkGenre[gen] = 0;
    genre[gen] = genre[gen] ? [...genre[gen], plays[i]] : [plays[i]];
    music[plays[i]] = music[plays[i]]
      ? [...music[plays[i]], i]
      : [i];
  }

  const revPlay = {};
  const tmp = [];
  for (let [key, value] of Object.entries(play)) {
    revPlay[value] = key;
    tmp.push(value);
  }

  for (let key of Object.keys(genre)) {
    
    genre[key].sort(function (a, b) {
      if (a > b) return -1;
      else if (b > a) return 1;
      else return 0;
    });

    if(genre[key].length > 2){
      genre[key]= genre[key].slice(0,2)
    }
    genre[key] = Array.from(new Set(genre[key]))
  }

  for(let key of Object.keys(music)){
    music[key].sort()

    if(music[key].length>2){
      music[key] = music[key].slice(0,2)
    }
  }

  tmp.sort(function (a, b) {
    if (a > b) return -1;
    else if (b > a) return 1;
    else return 0;
  });

  let arr = [];
  tmp.forEach((num) => {
    arr.push(revPlay[num]);
  });

  for(var gen of arr){
    var cnt = 0;
    for(var pl of genre[gen]){
      for(var song of music[pl]){
        if(cnt<2){
          cnt+=1;
          answer.push(song)
        }
      }
    }
  }



  return answer;
}