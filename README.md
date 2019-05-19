# Twitter Sentiment Analysis

Simple sentiment analysis of public tweets using Python 3.

Sentiment analysis is performed using TextBlob:
  - Positive sentiment: polarity > 0
  - Neutral sentiment: polarity = 0
  - Negative sentiment: polarity < 0

## Getting Started

Clone this repository.

### Prerequisites

Things you will need to have installed:
```
Python 3
```

You will also need to have a Twitter developer account and a registered App which will give allow you to generate the consumer keys and access tokens required for the API.

Make sure to include those in the code as specified by the placeholder strings:
```
consumer_key = 'your_consumer_key'
consumer_key_secret = 'your_secret_consumer_key'

access_token = 'your_access_token'
access_token_secret = 'your_secret_token'
```

### Installing

Navigate to the root of the project and execute the following command to install the related dependencies:
```
pip install -r requirements.txt
```

## How to Run/Deploy

Simply run main.py. With the current state of the project/code you should get console output which looks like this:
```
RT @Josh_Rager: $BTC - 3D chart Super Guppy

Amazing similarity between the last bear market prior to uptrend

Bitcoin had a similar parabo…

Sentiment(polarity=0.18666666666666668, subjectivity=0.4066666666666666)
====================================================================================================
RT @eucxio: #EUCX is registered with the SEC.

Accredited investors from the US can participate in the $EUCX #presale

#Register now at htt…

Sentiment(polarity=-0.1, subjectivity=0.6)
====================================================================================================
Happy #mothersday 

If you haven't sent your mom a Bitcoin you don't love her

Sentiment(polarity=0.65, subjectivity=0.8)
====================================================================================================
RT @orangebook_: I don’t meditate in a silent room alone.

I keep myself in chaotic environments.

Observe my judgmental/emotional reaction…

Sentiment(polarity=0.0, subjectivity=0.1)
====================================================================================================
🔄 Prices update in $USDT (1 hour):

$BTC - 7112.78 $ (+1.15 %)
$ETH - 188.98 $  (+0.65 %)
$XRP - 0.31 $    (+0.86 %… https://t.co/BwtUBQdUXR

Sentiment(polarity=0.0, subjectivity=0.0)
====================================================================================================
@TheoPaphitis Hi! My business is unusual. I am a bitcoin trader. By that I mean people come to me to buy bitcoin wo… https://t.co/OH32EpulVU

Sentiment(polarity=-0.056249999999999994, subjectivity=0.84375)
====================================================================================================
#cme #cmefutures #bitcoin #BTC

Sentiment(polarity=0.0, subjectivity=0.0)
====================================================================================================
RT @DrevZiga: @cz_binance We’ve used ODN, self-governed L2 @ethereum based network, to trace TXs of stolen funds, much like we’d do for a f…

Sentiment(polarity=0.2, subjectivity=0.2)
====================================================================================================
📌 La minería de Bitcoin contamina tanto al año como un millón de vuelos trasatlánticos https://t.co/00re9oVnvQ

Sentiment(polarity=0.0, subjectivity=0.0)
====================================================================================================
RT @mhschmidt2: So #DearMeTenYearsAgo is trending. What would I have told myself? 

“BUY A SHIT TON OF BITCOIN” 

also... 

“Don’t start th…

Sentiment(polarity=-0.2, subjectivity=0.8)
====================================================================================================
RT @AltcoinSara: In December of 2018, mainstream media proclaimed Bitcoin was dead. Bitcoin fell 84% from its ATH and investor interest dro…

Sentiment(polarity=-0.2, subjectivity=0.4)
====================================================================================================
RT @AaronvanW: I think @gladstein's gave one of the best "Why Bitcoin?" talks I have seen so far. #MCC2019 

https://t.co/3m9Fmu6iGf

Sentiment(polarity=0.55, subjectivity=0.65)
====================================================================================================
RT @tylerwinklevoss: Should we rename Blockchain Week to Bitcoin Week? 😂🚀👍

Sentiment(polarity=0.0, subjectivity=0.0)
====================================================================================================
The Hardware Bitcoin Wallet. Get Trezor now for only 89 EUR https://t.co/RyPUbEzrNS #btc #bitcoin 16 https://t.co/D11ihjIeGD

Sentiment(polarity=0.0, subjectivity=1.0)
====================================================================================================
Parabolic Advance Halts For Now – So What’s Next For Bitcoin Price? https://t.co/04U0GUOROv

Sentiment(polarity=0.0, subjectivity=0.0)
====================================================================================================
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Tweepy documentation: http://docs.tweepy.org/en/3.7.0/index.html
* TextBlob documentation: https://textblob.readthedocs.io/en/dev/
