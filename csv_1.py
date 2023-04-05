import csv

fieldnames = ["'id', 'URL', 'headline', 'author', 'date'"]
writer_list = [[" 01, https://www.theverge.com/2023/3/31/23664849/twitter-releases-algorithm-musk-open-source, Twitter takes its algorithm ‘open-source,’ as Elon Musk promised', Mitchell Clark, 2023/4/1"] 
, [" 02, https://www.theverge.com/2023/3/28/23659191/amazon-sidewalk-network-coverage, Amazon just opened up its Sidewalk network for anyone to build connected gadgets on, Jennifer Pattison Tuohy, 2023/4/1"] 
, [" 03, https://www.theverge.com/2023/3/31/23522169/how-to-fix-disney-plus-brightness-dark-hdr-dolby-vision’', Sean Hollister, 2023/4/1"]
, [" 04, https://www.theverge.com/2023/3/31/23665249/hoverboard-recall-jetson-rogue-cspc-recall-fire-risk, This hoverboard is being recalled after a fire that killed two children, Jay Peters, 2023/4/1"]
, [" 05, https://www.theverge.com/2023/3/31/23665128/marvel-secret-invasion-disney-plus-skrulls, Marvel’s Secret Invasion series actually sounds kind of fascinating, Charles Pulliam-Moore ,2023/4/1"]
, [" 06, https://www.theverge.com/2023/3/31/23664849/twitter-releases-algorithm-musk-open-source, The shape of Kirby, Ash Parrish, 2023/3/31"]
, [" 07, https://www.theverge.com/2023/3/31/23664923/twitter-verification-for-organizations-free-for-most-followed, Twitter’s $1,000 checkmark will be free for the 10,000 most-followed companies, Mitchell Clark, 2023/4/1"]
, [" 08, https://www.theverge.com/2023/3/31/23665215/sonic-the-hedgehog-murder-mystery-game-free-steam, The Murder of Sonic the Hedgehog is a new, real, and free game you can play right now', Antonio G. Di Benedetto, 2023/4/1"]
, [" 09, https://www.theverge.com/2023/3/31/23664767/plant-sounds-stress-tomato-tobacco-research, This is what a plant sounds like when it’s stressed, Justine Calma, 2023/4/1"]
, [" 010, https://www.theverge.com/2023/3/31/23664809/vampire-survivors-tides-of-the-foscari-fantasy-dlc-expansion-release-date, Vampire Survivors new fantasy-themed expansion launches in April for just $2, Jay Peters, 2023/3/31"]
, [" 011, https://www.theverge.com/2023/3/31/23664748/truckla-tesla-model-3-pickup-truck-update-simone-giertz-video, The ‘Truckla’ DIY Tesla pickup truck is still trucking, Umar Shakir, 2023/4/1"]
, [" 012, https://www.theverge.com/2023/3/31/23664595/amazon-boys-come-first-aaron-foley-chuck-hayward, Amazon to adapt Aaron Foley’s Boys Come First as a new series, Charles Pulliam-Moore, 2023/3/31"]
, [" 013, https://www.theverge.com/2023/3/31/23664636/federal-ev-tax-credit-vehicles-qualify-eligible-battery-china, Fewer EVs will qualify for the federal $7,500 tax credit under updated rules, Andrew J. Hawkins, 2023/3/31"]
, [" 014, https://www.theverge.com/2023/3/31/23663053/google-pixel-6-pro-playstation-store-spring-sale-belkin-3-in-1-charger-ray-ban-stories-deal, Google’s last-gen Pixel 6 Pro is half off right now at Woot, Sheena Vasani, 2023/3/31"]
, [" 015, https://www.theverge.com/23200304/ios-16-beta-install-apple-how-to, How to install the latest iOS 16 and iPadOS 16 public betas, Umar Shakir, 2023/3/31"]
, [" 016, https://www.theverge.com/23664519/ai-industry-pause-open-letter-societal-harms, Why the AI industry could stand to slow down a little, Casey Newton, 2023/3/31"]
, [" 017, https://www.theverge.com/2023/3/31/23664451/italy-bans-chatgpt-over-data-privacy-laws, Italian regulators order ChatGPT ban over alleged violation of data privacy laws, James Vincent, 2023/3/31"]
, [" 018, https://www.theverge.com/2023/3/31/23664437/virgin-orbit-layoffs-cease-operations-satellite-launch, Virgin Orbit to cease all operations and lay off 85 percent of its workforce, Jess Weatherbed, 2023/3/31"]
, [" 019, https://www.theverge.com/2023/3/31/23664426/google-bard-ai-chatbot-upgrades-coming-soon-sundar-pichai,Google CEO Sundar Pichai promises Bard AI chatbot upgrades soon: ‘We clearly have more capable models’, James Vincent, 2023/3/31"]
, [" 020, 'https://www.theverge.com/2023/3/30/23664044/e3-cancelled-isnt-coming-back, E3 isn’t coming back, Jay Peters, 2023/3/31"]]

with open("ddmmyyy_verge.csv", mode='w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(writer_list)