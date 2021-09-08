# Format of training prompt
defaultPrompt = """I am an intelligent email assistant that can generate the following emails from the descriptive input:
Input: Thank John for the book, John is a childhood friend who gifted me a book last week on my birthday.

Output:
Dear John,

Hope you are doing well. 

Thank you so much for giving such a precious gift.

I really appreciate this gesture amd hope to hang out soon. 

Your friend,
-


Input: Tell TechCorp I appreciate the great service, I visted the TechCorp showroom last weekend wherre I was very impressed by the warmth and great service of their staff

Output:
To Whom it May Concern,

I want you to know that I appreciate the great service at TechCorp.

The staff is outstanding and I enjoy every visit.

Sincerely,
-


Input: Invite Amanda and Paul to the company event Friday night. Amanda and Paul are close friends. This friday we are celebrating the five year anniversary for zolotech

Output:
Hey Guys,

I hope this finds you doing well.

With great joy and immense plesure I would like to invite you to the fith anniversary celebration for zolotech.

Looking forward to seeing you there.

Your friend,
-


Input: Invoice Kelly Watkins $500 for design consultation. Last week I have consulted kelly for five hours in her opensource design project enigma.

Output:

Dear Ms. Watkins,

Sending you an invoice of $500 for helping you with your project Enigma.

It was a pleasure to work with you.

Sincerely,
-


Input: Thank Sarah for a great meal. I am Patrick and Sarah is my wife, she bought me a great lunch this afternoon

Output:
Dear Sarah,

Thank you so much for a great meal today.

It was very delicious and I really enjoyed it.

I appreciate the effort you put in for this.

Please do keep this up.

You are a great cook.

Love,
-


Input: Ask Jane to send the release doc to Google corp. Jane is my secretary, she has the release documents for LendKart application, which is a peer-to-peer lending platform

Output:
Jane,

Please send the release documents for the LendKart application to Google corp.

They have been asking me for the same.

Thanks,
-


Input: Introduce the new Customer Support Representative to the team. Ram currently started working as Customer Rep for Xolo Corp

Output:
Hi Team,

I would like to introduce you to Ram, who is our new Customer Rep.

He has been with us for a week now and I am sure you will love working with him.

Please make him feel welcome.

Thanks,
-


Input: complaint for bad quality headphones. Recently purchased Boat headphones from amazon

Output:
Dear Sir,

I am writing this email to express my concern about the quality of the headphones I purchased from your company.

I bought a Boat headphone from amazon last week.

The sound quality is very poor and I am not satisfied with the product.

I would like to request you to either replace the product or refund my money.

Thank you,
-


Input: {}

Output: """