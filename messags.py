initial_convo = ['''Guest: Hi there! I just booked your place for next weekend. I'm so excited!
Host: Hello! That's great news, we're thrilled to have you. Is there anything specific you'd like to know about the area or the accommodation before your visit?

Guest: Actually, do you have any recommendations for local restaurants or cool places to visit nearby?
Host: Absolutely! There's a fantastic Italian restaurant just a few blocks away, and a beautiful park perfect for morning walks. I'll send you a list of my favorite spots in the neighborhood.''',
         '''Guest: Hi, I hope you're doing well! We just checked in, and the place looks amazing. Thank you for the detailed instructions.
Host: Hi! I'm glad you found everything alright. If you need anything during your stay or have any questions about the area, feel free to reach out anytime.

Guest: Thank you so much! By the way, is there a grocery store nearby?
Host: Yes, there's a market about a 10-minute walk from here. If you need directions or recommendations for specific items, let me know''',
         '''Guest: Hey, we're loving the place so far! It's even better than the photos.
Host: Hi! I'm delighted to hear that you're enjoying your stay. If there's anything you need or if any issues come up, please don't hesitate to let me know.

Guest: Thanks! Do you have any suggestions for fun activities to do in the evenings around here?
Host: Absolutely! There's a great live music venue just a short drive away, and a cozy bar with a fantastic cocktail menu within walking distance. I'll send you more details.''',
         '''Guest: Hi, we just got in. The place is lovely, thank you!
Host: Hello! I'm thrilled you like it. If there's anything I can assist you with during your stay or if you need any local recommendations, feel free to ask.

Guest: Thanks! Is there a public transportation option nearby to get around the city easily?
Host: Yes, there's a bus stop just a few blocks away that can take you to downtown in about 20 minutes. I can provide you with a schedule and some tips for getting around.''',
         '''
Guest: Hi there! I just booked your place for next weekend. I'm so excited!
Host: Hello! That's great news, we're thrilled to have you. Is there anything specific you'd like to know about the area or the accommodation before your visit?

Guest: Actually, do you have any recommendations for local restaurants or cool places to visit nearby?
Host: Absolutely! There's a fantastic Italian restaurant just a few blocks away, and a beautiful park perfect for morning walks. I'll send you a list of my favorite spots in the neighborhood.''',
'''
Guest: Hi, I hope you're doing well! We just checked in, and the place looks amazing. Thank you for the detailed instructions.
Host: Hi! I'm glad you found everything alright. If you need anything during your stay or have any questions about the area, feel free to reach out anytime.

Guest: Thank you so much! By the way, is there a grocery store nearby?
Host: Yes, there's a market about a 10-minute walk from here. If you need directions or recommendations for specific items, let me know.
''',
                 '''
Guest: Hey, we're loving the place so far! It's even better than the photos.
Host: Hi! I'm delighted to hear that you're enjoying your stay. If there's anything you need or if any issues come up, please don't hesitate to let me know.

Guest: Thanks! Do you have any suggestions for fun activities to do in the evenings around here?
Host: Absolutely! There's a great live music venue just a short drive away, and a cozy bar with a fantastic cocktail menu within walking distance. I'll send you more details.
''','''
Guest: Hi, we just got in. The place is lovely, thank you!
Host: Hello! I'm thrilled you like it. If there's anything I can assist you with during your stay or if you need any local recommendations, feel free to ask.

Guest: Thanks! Is there a public transportation option nearby to get around the city easily?
Host: Yes, there's a bus stop just a few blocks away that can take you to downtown in about 20 minutes. I can provide you with a schedule and some tips for getting around.
''','''
Guest: Hi, we're settled in, and everything is fantastic. Your place is stunning!
Host: Hi there! I'm so happy to hear that you're comfortable. If you need anything or want suggestions for nearby attractions or restaurants, just let me know.

Guest: Thank you! By the way, are there any hiking trails or parks nearby that we should explore?
Host: Yes, there's a beautiful nature reserve about a 15-minute drive away with hiking trails and breathtaking views. I'll send you more information about it.''',
         '''Guest: Hi, I'm interested in renting your place for a few days next month. Could you provide more information about the check-in and check-out times?
Host: Hello! Sure, our standard check-in time is after 3 PM, and check-out is by 11 AM. However, we can be flexible depending on your travel schedule. Let me know your preferred times.

Guest: Thank you! Also, is there a security deposit or any additional fees I should be aware of?
Host: We do require a security deposit, which is fully refundable after your stay, provided there are no damages. There's also a cleaning fee included in the booking.''',
                 '''Guest: Hi there! Your place looks amazing, and I'm considering renting it for a week. Just wanted to check if there's a minimum stay requirement?
Host: Hello! Thank you for your interest. We do have a minimum stay of three nights, but for longer stays like yours, we offer discounted rates.

Guest: Great to know! Are utilities like water, electricity, and internet included in the rental cost?
Host: Yes, all utilities are included in the rental cost, so you won't have to worry about any additional charges for those during your stay.''',
    '''Guest: Hello, I'm planning a trip and your place seems perfect! Could you clarify if there's a cancellation policy in case my plans change?
Host: Hi! I'm glad you're considering staying with us. We have a moderate cancellation policy, which allows for a full refund if you cancel within 5 days of the reservation.

Guest: Thank you! Is there a process for key exchange or entry into the property upon arrival?
Host: Yes, we usually arrange a convenient time to meet for key exchange, or we have a lockbox system for self-check-in. Whichever option suits you best.''',
                 '''Guest: Hi, your place looks lovely! I'm interested in renting it for a weekend getaway. Could you confirm if there's a pet policy?
Host: Hello! Thank you. We do allow pets, but there's an additional pet fee. Please let me know if you plan to bring a pet, so I can provide more details.

Guest: That's great! Just to confirm, is there parking available at your property?
Host: Yes, we have parking available for one vehicle. If you have more than one car, there's street parking nearby, which is usually quite convenient.''',
                 '''Guest: Hi, I'm considering renting your place for a month-long stay. Do you offer any discounts for longer bookings?
Host: Hello! Absolutely, for extended stays like that, we offer a discounted rate. Let me know your exact dates, and I'll provide you with the adjusted pricing.

Guest: Thank you! Could you provide more information about the amenities available, like laundry facilities or kitchen equipment?
Host: Sure, we have a washer and dryer on-site for your use, and the kitchen is fully equipped with everything you might need during your stay.''']


mid_convos = ['''Guest: Hi! Just checked in. The place is amazing, but the TV remote seems to be missing.
Host: Oh no! I apologize for the inconvenience. I'll have a spare remote brought to you right away.

Guest: No worries, thank you! Also, the view from here is breathtaking.
Host: I'm glad you like it! There's a great spot for sunset views just a short walk away too.''',
              '''Guest: Hi, quick question. Is it okay if we have a small gathering tonight for a birthday celebration?
Host: Of course, happy birthday! Just please be mindful of noise levels after 10 PM so as not to disturb the neighbors.

Guest: Thank you! We'll keep it low-key. Appreciate your understanding.''',
              '''Guest: Hi, the shower drain seems to be a bit clogged.
Host: I'm sorry to hear that. I'll send our maintenance person over to take care of it ASAP.

Guest: Thanks, I appreciate it. Other than that, everything's been perfect.''',
              '''Guest: Hi! The Wi-Fi seems to be a bit slow. Is there anything we can do to improve it?
Host: I'll look into it right away. Sometimes resetting the router helps. I'll send you instructions.

Guest: Thanks, that would be great. We really appreciate your help.''',
              '''Guest: Hey, do you have any board games or cards we could use during our stay?
Host: Absolutely! There's a collection of games in the living room cabinet. Enjoy!

Guest: Awesome, thanks a lot! You've been so accommodating.''',
              '''Guest: Hi! We just arrived and the place looks great.

Host: Hello! Glad you made it safely. If you need anything during your stay, feel free to ask.

Guest: Thanks! The weather is quite nice today.

Host: Yes, it is. It's been pretty unpredictable lately though.

Guest: Oh, really? Do you get a lot of rain around here?

Host: Sometimes, but not too much. It varies throughout the year.

Guest: I see. I like the decor in this room.

Host: Thank you! We tried to make it comfortable for guests.

Guest: It's definitely cozy. So, what are some popular attractions nearby?

Host: There's a museum downtown and a beautiful park a few blocks away.

Guest: Sounds nice. How far is the park from here?

Host: It's about a 10-minute walk.

Guest: Oh, that's not too bad.

Host: No, it's quite pleasant.

Guest: Well, thanks for the information.

Host: Of course, anytime.''',
              '''Guest: Hi, just wanted to say the place is lovely.
Host: Thank you! I'm glad you like it. Is there anything specific you need during your stay?

Guest: No, all good. Just wanted to mention it's nice''',
              '''Guest: Hi, do you have any recommendations for things to do around here?
Host: Absolutely! There are museums, parks, and great restaurants nearby. What are you interested in?

Guest: Hmm, I'm not sure yet. Just wanted to ask.''',
              '''Guest: Hi, we're arriving tomorrow. Can you tell us how to get there from the airport?
Host: Sure! There are a few options—shuttle, taxi, or public transport. Which one are you considering?

Guest: I'm not sure yet, just wanted to ask for information.''',
              '''Guest: Hi, I noticed there's a small leak in the bathroom.
Host: Oh no! I'll send someone to fix it right away. Is it causing any inconvenience?

Guest: It's manageable. Just wanted to let you know.''',
              '''Guest: Hi, we're thinking of exploring the town. Any must-see places?
Host: Definitely! The historic district and the local market are worth visiting. Are you looking for anything specific?

Guest: Not really, just wanted to know what's around.''',
              '''Guest: Hi, I was wondering if you had any recommendations for local attractions in the area.
Host: Absolutely! There's a beautiful museum downtown and a stunning hiking trail nearby.

Guest: Oh, that sounds great! I've been to a few museums lately, though. How's the weather been around here?
Host: It's been quite pleasant lately, not too hot or too cold.

Guest: Yeah, weather can really affect plans. I remember one time...''',
              '''Guest: Hi, do you have any tips for restaurants nearby?
Host: Oh, there are a few fantastic places within walking distance. One serves excellent Italian cuisine.

Guest: Italian food sounds nice! I'm a vegetarian though, do they have many veg options?
Host: Yes, they do have some vegetarian dishes that are quite popular.

Guest: That's good to hear. Speaking of vegetarianism, I've been experimenting with new recipes...''',
              '''Guest: Hi, I'm interested in booking your place for a weekend getaway.
Host: That's wonderful! Our calendar is open for those dates.

Guest: Perfect! By the way, what's the best mode of transportation to get to your place from the airport?
Host: There are taxis, shuttles, and even a train that you can take.

Guest: I've never been on a train before. Have you taken the train often?''',
              '''Guest: Hi, I was wondering if your place has a gym or fitness facilities nearby.
Host: Yes, there's a gym just a couple of blocks away that guests can access.

Guest: Oh, that's convenient! I've been trying to keep up with my fitness routine. How about you?
Host: I do enjoy staying active, going for walks mostly.

Guest: Walking is great for staying active. I once went on this long hike...''']

end_convos = ['''Guest: Hi, thank you for providing all the details about your place. It looks lovely, but after considering it further, I've decided to explore other options for my stay.
Host: Hello! I completely understand. If there's anything specific that didn't meet your expectations or if you need further information, feel free to let me know. I hope you find the perfect accommodation for your trip.''',
                 '''Guest: Hi there, I appreciate your prompt responses and the information about your rental. However, I've found another place that aligns better with my travel plans.
Host: Hello! Thank you for considering my place. I'm glad you found suitable accommodation. If your plans change or if you have friends visiting in the future, feel free to reach out. Have a wonderful trip!''',
                 '''Guest: Hi, your place seems fantastic, but upon further consideration, I've decided to go for a different location that's closer to the event I'll be attending.
Host: Hello! I completely understand. Location is crucial, and I'm glad you found something more suitable for your needs. If you ever need a place in the area in the future, don't hesitate to reach out. Enjoy your event!''',
                 '''Guest: Hello, thank you for all the details about your rental. It's a beautiful place, but I've had a change in my travel plans and will be staying elsewhere.
Host: Hi! I appreciate your consideration. I understand how plans can change. If you ever find yourself back in this area or if your plans shift again, feel free to check if my place is available. Safe travels!''',
                 '''Guest: Hi, I've been looking at various options and while your place is wonderful, I've decided to go with a different style of accommodation that suits my preferences a bit better.
Host: Hello! Thank you for letting me know. I'm glad you found something that fits your preferences. If your plans ever bring you back this way or if you have any friends visiting, feel free to recommend my place. Wishing you a fantastic stay!'''

                 ]

##initial_guest = []
##initial_host = []
##for x in initial_convo:
##    for y in x.split('\n'):
##        if y not in [' ', '']:
##            if 'Guest: ' in y:
##                initial_guest.append(y[7:])
##            elif 'Host: ' in y:
##                initial_host.append(y[5:])


##mid_guest, mid_host = [],[]
##for x in mid_convos:
##    for y in x.split('\n'):
##        if y not in [' ', '']:
##            if 'Guest: ' in y:
##                mid_guest.append(y[7:])
##            elif 'Host: ' in y:
##                mid_host.append(y[5:])
##
##end_guest, end_host = [],[]
##for x in end_convos:
##    for y in x.split('\n'):
##        if y not in [' ', '']:
##            if 'Guest: ' in y:
##                end_guest.append(y[7:])
##            elif 'Host: ' in y:
##                end_host.append(y[5:])
                
##for x in initial_guest:
##    print(repr(x))

import mariadb
import datetime as dt
import random as r

# Connect to MariaDB Platform
conn = mariadb.connect( user="root", password="password", host="127.0.0.1", port=3306, database="airbnb" )

# Get Cursor
cur = conn.cursor()
# get data from booking table
cur.execute('SELECT guestID, listingID, booking_date, check_in, status FROM booking')

guestID, hostID, booking_date, check_in, status = [],[],[],[],[]
for gid, hid, bd, co, stat in cur:
    guestID.append(gid)
    hostID.append(hid)
    booking_date.append(bd)
    check_in.append(co)
    status.append(stat)

##for msg in guestID:
##    if status[msg] != 'cancelled':
##        for x in initial_convo:
##            for y in x.split('\n'):
##                if y not in [' ', '']:
##                    if 'Guest: ' in y:
##                        mesag = y[7:]
##                        msgbyhost = 0
##                    elif 'Host: ' in y:
##                        mesag = y[5:]
##                        msgbyhost = 1

with open(r'insert ddl\messages.txt', 'a') as file:
    for guest in range(2,18):
        select_hosts = r.randint(1,19)
        random_hosts = []
        for h in range(1,select_hosts):
            random_hosts.append(h)
        for host in random_hosts:
            i_msgs = r.choice(initial_convo)
            d = dt.datetime.combine(booking_date[guest], dt.time.min)
            d = d- dt.timedelta(days=r.randint(3,11), hours=r.randint(0,24), minutes=r.randint(0,60), seconds=r.randint(0,60))
            for msg in i_msgs.split('\n'):
                d = d + dt.timedelta(seconds = len(msg))
                if msg not in [' ', '']:
                    if 'Guest: ' in msg:
                        msgbyhost = 0
                        f"(NULL,{guest},{host},'{d}'," + f'"{msg[7:]}",{msgbyhost}),\n'
                        file.write(f"(NULL,{guest},{host},'{d}'," + f'"{msg[7:]}",{msgbyhost}),\n')
                    elif 'Host: ' in msg:
                        msgbyhost = 1
                        file.write(f"(NULL,{guest},{host},'{d}'," + f'"{msg[5:]}",{msgbyhost}),\n')

            if status[guest] != 'cancelled':
                m_msgs = r.choice(mid_convos)
                d = dt.datetime.combine(check_in[guest], dt.time.min)
                for msg in m_msgs.split('\n'):
                    d = d + dt.timedelta(minutes = len(msg))
                    if msg not in [' ', '']:
                        if 'Guest: ' in msg:
                            msgbyhost = 0
                            file.write(f"(NULL,{guest},{host},'{d}'," + f'"{msg[7:]}",{msgbyhost}),\n')
                        elif 'Host: ' in msg:
                            msgbyhost = 1
                            file.write(f"(NULL,{guest},{host},'{d}'," + f'"{msg[5:]}",{msgbyhost}),\n')
            else:
                e_msgs = r.choice(end_convos)
                d = dt.datetime.combine(booking_date[guest], dt.time.min)
                for msg in e_msgs.split('\n'):
                    d = d + dt.timedelta(minutes = len(msg))
                    if msg not in [' ', '']:
                        if 'Guest: ' in msg:
                            msgbyhost = 0
                            file.write(f"(NULL,{guest},{host},'{d}'," + f'"{msg[7:]}",{msgbyhost}),\n')
                        elif 'Host: ' in msg:
                            msgbyhost = 1
                            file.write(f"(NULL,{guest},{host},'{d}'," + f'"{msg[5:]}",{msgbyhost}),\n')

