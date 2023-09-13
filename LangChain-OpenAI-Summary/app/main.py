from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Body, Request
from urllib.parse import unquote
from app.model.model import prediction_pipeline

model_version = 1.0

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/")
def home():
    result = {"health_check": "OK", "model_version": model_version}
    return result

@app.post("/predict")
def summary_generator(text):

    predicted_summary = prediction_pipeline(text)
    print("Here is the Complete Summary", predicted_summary)
    response= {
        # 'submitted_url': encode_url,
        'summary': predicted_summary
    }
    return response



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=80)

# text = "Coco Gauff, the world No. 10 women’s singles player, has defeated Belarusian Aryna Sabalenka 2-6 6-3 6-2 with a dramatic comeback in the women’s US Open final.The star-studded crowd erupted with applause after Gauff’s home-turf victory at Arthur Ashe Stadium in Queens. The win is 19-year-old Gauff’s first career grand slam and makes her the first American teenager to win the US Open since 23-time major champion Serena Williams took the title in 1999.I feel like I’m in shock at this moment,” said an emotional Gauff after her win. “God puts you through tribulations and trials, and that makes this moment sweeter than I would have imagined.She thanked her family, her team, and “the people who didn’t believe in me.”Bidding for her second major title of the year, the soon-to-be women’s world No. 1 Sabalenka made quick work in the first set, breaking Gauff’s serve three times to win 6-2 in dominant fashion.However, with the packed crowd chanting “Let’s go Coco,” Gauff raised her level in the second set, going up a break before eventually taking it 6-3 to force a deciding third set.A locked-in Gauff took control in the third set, going up a double break to inch ever closer to her maiden grand slam title. Although Sabalenka took the next two games, Gauff closed out the match to become the 12th teenager in US Open history to win the title.“I don’t know, I just knew that if I didn’t give it my all, I had no shot at winning,” Gauff said on how she found the strength to rally after dropping the first set.In her run to the final, the athlete twice lost the first set of a match, once in the first round against Laura Siegemund and again in the third round against Elise Mertens.With the victory, Gauff becomes the third American teenager to win the US Open title, joining Williams and Tracy Austin. She is set to move up to No. 3 in the WTA singles rankings, and co-No. 1 in doubles along with compatriot Jessica Pegula.After clinching the victory, Gauff dropped to the ground before getting up to hug Sabalenka. Afterward, Gauff was overcome with emotion and knelt down to take in the moment.Gauff poked fun at her father after the match as she thanked her family. “Thank you first to my parents,” she said. “Today was the first time I’ve ever seen my dad cry. He doesn’t want me to tell y’all that, but he got caught in 4K!”Gauff also told reporters her parents helped when she would be too self-critical, placing too much value in whether she won or lost.“I used to put my tennis and compare it to like my self-worth. When I would lose, I would think, you know, I was not worth it as a person. So having my parents always remind me that they love me regardless of how I do helped me today.”When asked the significance of being the latest Black woman to win the women’s singles title, Gauff credited prior champions such as Venus Williams and Serena Williams, who “paved the way for me to be here” and added she was inspired by seeing Sloane Stephens win the US Open in 2017.“I hope that another girl can see this and believe that they can do it, and hopefully their name can be on this trophy, too,” she said.Meanwhile, despite the loss, the Belarusian star will move to No. 1 in the WTA singles rankings on Monday, ending Iga Świątek’s 75-consecutive week reign.Sabalenka congratulated her competitor, saying, “I hope we play in many more finals” and calling Gauff “amazing.”The American in turn congratulated Sabalenka on her rise to the No. 1 position. “Aryna is an incredible player,” she said. “Congratulations on the No. 1 ranking, it’s well deserved.”At a news conference after the match, Sabalenka said the loss was a “lesson” for her and she had started “overthinking” during the second set.“It’s me against me,” she said. Gauff “was moving really and defending better than anybody else.”“I was playing against the crowd,” she added.The last time Gauff and Sabalenka met was in the quarterfinals of Indian Wells in March, with the Belarusian winning comfortably, 6-4 6-0. Saturday’s final was an altogether different contest, however, with Gauff having improved rapidly in the six months that have passed since that defeat.The 19-year-old has won three WTA titles this season, including the biggest of her career in Cincinnati just before the US Open.The competition was the second grand slam final of Gauff’s career after reaching the French Open final in 2022, where she was swiftly defeated by Iga Świątek.Following her 6-4 7-5 semifinal win over Karolína Muchová, Gauff spoke about the improvement in her mentality, going from somebody blighted by imposter syndrome to now believing she is capable of contending with the best players in the world.She is not only contending but can now be regarded as one of the best players in the world after this win.Gauff was facing a formidable opponent – the best player in the world. Until her semifinal against Madison Keys, Sabalenka had been dominant in New York – not dropping a set and never losing more than five games in a match.However, despite defeat Sabalenka’s run to the final has capped a remarkable year in which she won three titles – including her first grand slam at the Australian Open and her sixth Masters 1000 title in Madrid."
# summary_generator(text)
