 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MeteorStrike - Stop Ignoring Your Customers</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@900&family=Roboto:wght@400;700;900&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#d5daeb',
                        secondary: '#ee4266',
                        accent: '#1c1259',
                        highlight: '#fcd307',
                    },
                    fontFamily: {
                        urbanist: ['Urbanist', 'sans-serif'],
                        roboto: ['Roboto', 'sans-serif'],
                    },
                }
            }
        }
    </script>
    <style>
        .pulse-warning {
            animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: .7;
            }
        }
        .shake-on-hover:hover {
            animation: shake 0.5s;
        }
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
            20%, 40%, 60%, 80% { transform: translateX(5px); }
        }
        .text-shadow-brutal {
            text-shadow: 4px 4px 0px rgba(0,0,0,0.8);
        }
        .border-brutal {
            border: 5px solid #000;
            box-shadow: 8px 8px 0px rgba(0,0,0,0.9);
        }
        .shadow-brutal {
            box-shadow: 8px 8px 0px rgba(0,0,0,0.9);
        }
    </style>
    <link rel="stylesheet" href="style.css">
    <script src="components/navbar.js"></script>
    <script src="components/footer.js"></script>
</head>
<body class="bg-accent text-primary font-roboto">
    <custom-navbar></custom-navbar>
    
    <!-- Hero Section -->
    <section class="min-h-screen flex items-center justify-center bg-gray-900 relative overflow-hidden">
        <div class="absolute inset-0 bg-black opacity-85"></div>
        <img src="https://huggingface.co/spaces/zebhead/brutal-feedback-blitzkrieg/resolve/main/images/Image%2018-11-2025%20at%2018.33.jpeg" 
             alt="Reviews are piling up" 
             class="absolute inset-0 w-full h-full object-cover">
        <div class="container mx-auto px-6 text-center relative z-10">
            <div class="bg-secondary border-brutal p-8 mb-8 inline-block pulse-warning">
                <h1 class="text-7xl md:text-9xl font-urbanist text-primary font-black text-shadow-brutal leading-none">
                    REVIEWS ARE COMING<br/>
                    <span class="text-highlight">DEAL WITH THEM</span>
                </h1>
            </div>
            <p class="text-3xl md:text-4xl font-roboto font-bold text-primary mb-8 bg-accent/80 p-4 inline-block">
                Your customers are talking about you.<br/>
                <span class="text-secondary text-4xl md:text-5xl font-black">Are you listening?</span>
            </p>
            
            <a href="#problem" class="bg-secondary hover:bg-highlight text-accent font-urbanist text-2xl md:text-3xl px-12 py-6 transition-all duration-300 inline-block border-brutal shake-on-hover font-black">
                SEE THE DAMAGE →
            </a>
        </div>
    </section>
 <p class="text-3xl md:text-4xl font-roboto font-bold text-primary mb-12 bg-accent/80 p-4 inline-block">
    88% of businesses ignore their customers<br/>
    <span class="text-secondary text-5xl">Don't be one of them</span>
</p>
 <!-- What You're Losing Section -->
<section class="min-h-screen flex items-center justify-center bg-secondary text-primary py-20">
    <div class="container mx-auto px-6 text-center">
        <div class="bg-accent border-brutal p-8 mb-12 inline-block">
            <h2 class="text-6xl md:text-8xl font-urbanist font-black text-highlight text-shadow-brutal">
                TICK. TOCK.
            </h2>
        </div>
        <h3 class="text-4xl md:text-6xl font-urbanist font-black mb-8 text-primary">
            Another unanswered review.<br/>
            Another lost customer.<br/>
            <span class="text-highlight text-5xl md:text-7xl">Another win for your competitor.</span>
        </h3>
        
        <div class="max-w-4xl mx-auto bg-accent p-12 text-primary border-brutal mt-16">
            <p class="text-2xl md:text-3xl mb-8 font-bold leading-relaxed">
                Every ignored review costs you <span class="text-highlight font-black">15 potential customers</span>. 
            </p>
            <p class="text-xl md:text-2xl mb-8 leading-relaxed">
                That angry customer? They're not suffering in silence. They're telling their mates, their family, their Facebook group. 
            </p>
            <div class="bg-secondary p-6 mb-8 border-4 border-black">
                <p class="text-2xl font-black">
                    5 bad reviews × 15 people = 75 customers gone.<br/>
                    <span class="text-highlight text-3xl">Per month.</span>
                </p>
            </div>
            <p class="text-xl mb-8">
                How long before there's nobody left to ignore?
            </p>
            <a href="#calculator" class="bg-highlight hover:bg-primary text-accent font-urbanist text-2xl md:text-3xl px-12 py-6 transition-all duration-300 inline-block border-4 border-black font-black shake-on-hover">
                SEE YOUR DAMAGE →
            </a>
        </div>
    </div>
</section>
 <!-- The Wake-Up Call Section -->
    <section class="min-h-screen flex items-center justify-center bg-gray-900 py-20">
        <div class="container mx-auto px-6 text-center">
            <div class="bg-highlight border-brutal p-8 mb-12 inline-block">
                <h2 class="text-4xl md:text-6xl font-urbanist font-black text-accent mb-4">
                    "What Doesn't Kill You..."
                </h2>
                <p class="text-5xl md:text-7xl font-urbanist text-secondary font-black">
                    ...IS KILLING YOUR BUSINESS
                </p>
            </div>
            <div class="max-w-2xl mx-auto bg-accent p-12 text-primary border-brutal">
                <p class="text-2xl md:text-3xl mb-8 font-bold leading-relaxed">
                    We work <span class="text-highlight font-black">24/7/365</span> to monitor and respond to EVERY. SINGLE. REVIEW. 
                </p>
                <p class="text-xl mb-12 text-primary/80">
                    So you don't have to lose sleep over lost customers. (You're welcome.)
                </p>
                <div class="bg-secondary p-6 mb-8">
                    <p class="text-lg font-bold">Professional responses. Zero embarrassment. Maximum damage control.</p>
                </div>
                <div class="flex flex-col md:flex-row gap-6 justify-center">
                    <a href="https://zebhead-meteorstrike-calculator.static.hf.space/" class="bg-highlight hover:bg-primary text-accent font-urbanist text-xl md:text-2xl px-10 py-5 transition-all duration-300 inline-block border-4 border-black font-black shake-on-hover">
                        💸 HOW MUCH AM I LOSING?
                    </a>
                    <a href="/pricing" class="bg-secondary hover:bg-highlight text-primary font-urbanist text-xl md:text-2xl px-10 py-5 transition-all duration-300 inline-block border-4 border-black font-black shake-on-hover">
                        🛡️ GET PROTECTION NOW
                    </a>
                </div>
            </div>
        </div>
    </section>
<!-- Comparison Section: The Three Types of Response -->
<section id="comparison" class="min-h-screen flex items-center justify-center bg-accent text-primary py-20">
    <div class="container mx-auto px-6">
        <div class="text-center mb-16">
            <h2 class="text-5xl md:text-6xl font-urbanist font-black mb-6">
                "We Value Your Feedback"
            </h2>
            <p class="text-3xl md:text-4xl font-urbanist text-secondary mb-4">
                [Proceeds to Ignore It]
            </p>
            <p class="text-xl max-w-2xl mx-auto">
                Most restaurants either ignore reviews completely, or respond with meaningless waffle. <span class="font-black">Both achieve exactly nothing.</span>
            </p>
        </div>

        <!-- Customer Review -->
        <div class="max-w-6xl mx-auto mb-12">
            <div class="bg-white border-brutal p-6">
                <p class="text-lg font-urbanist font-bold text-gray-800">
                    ⭐⭐ Customer Review: "Delivery took 90 minutes and the food arrived cold. Really disappointed."
                </p>
            </div>
        </div>

        <!-- Three Response Boxes -->
        <div class="grid md:grid-cols-3 gap-6 max-w-6xl mx-auto">
            
            <!-- BOX 1 - Total Ignore -->
            <div class="relative">
                <div class="bg-gray-300 border-4 border-gray-500 p-6 opacity-60 min-h-[300px] flex flex-col">
                    <div class="absolute -top-4 left-4 bg-red-700 text-white px-4 py-2 font-urbanist font-black text-xs">
                        ❌ USELESS
                    </div>
                    <div class="mt-8 flex-1 flex items-center justify-center">
                        <div class="text-center">
                            <p class="text-6xl mb-4">🦗</p>
                            <p class="text-2xl font-urbanist font-black text-gray-600">
                                *CRICKETS*
                            </p>
                            <p class="text-sm text-gray-600 mt-4">
                                No response at all
                            </p>
                        </div>
                    </div>
                    <div class="mt-4 pt-4 border-t-2 border-gray-500">
                        <p class="text-xs text-gray-700 font-bold">
                            ✗ Issue: Not addressed<br>
                            ✗ Customer: Still angry<br>
                            ✗ Outcome: Lost forever
                        </p>
                    </div>
                </div>
            </div>

            <!-- BOX 2 - Generic Rubbish -->
            <div class="relative">
                <div class="bg-gray-300 border-4 border-gray-500 p-6 opacity-60 min-h-[300px] flex flex-col">
                    <div class="absolute -top-4 left-4 bg-red-700 text-white px-4 py-2 font-urbanist font-black text-xs">
                        ❌ EQUALLY USELESS
                    </div>
                    <div class="mt-8 flex-1">
                        <div class="bg-white p-4 border-2 border-gray-500">
                            <p class="text-sm text-gray-700 italic">
                                "Thank you for your feedback! We value all our customers and strive to provide excellent service. Your opinion matters to us!"
                            </p>
                        </div>
                    </div>
                    <div class="mt-4 pt-4 border-t-2 border-gray-500">
                        <p class="text-xs text-gray-700 font-bold">
                            ✗ Issue: Not addressed<br>
                            ✗ Customer: Still angry<br>
                            ✗ Outcome: Lost forever
                        </p>
                    </div>
                </div>
            </div>

            <!-- BOX 3 - MeteorStrike -->
            <div class="relative">
                <div class="bg-secondary border-brutal p-6 shadow-brutal min-h-[300px] flex flex-col">
                    <div class="absolute -top-4 left-4 bg-primary text-accent px-4 py-2 font-urbanist font-black text-xs border-2 border-primary">
                        ✓ ACTUALLY USEFUL
                    </div>
                    <div class="mt-8 flex-1">
                        <div class="bg-accent p-4 border-4 border-primary">
                            <p class="text-sm text-primary font-medium">
                                "90 minutes is not acceptable - sorry about that. We've had a word with the driver and we're sorting our delivery routing. Cold food is even worse. Give us another shot - mention this review and if it's not spot on, meal's on us."
                            </p>
                        </div>
                    </div>
                    <div class="mt-4 pt-4 border-t-4 border-primary">
                        <p class="text-xs font-bold">
                            ✓ Issue: Acknowledged & fixed<br>
                            ✓ Customer: Feels heard<br>
                            ✓ Outcome: Second chance earned
                        </p>
                    </div>
                </div>
            </div>

        </div>

        <!-- Callout Between Bad Responses -->
        <div class="max-w-6xl mx-auto mt-8 mb-12">
            <div class="bg-red-100 border-4 border-red-700 p-6 text-center">
                <p class="text-xl font-urbanist font-black text-red-900">
                    SPOILER: Both responses on the left achieve EXACTLY THE SAME RESULT.<br>
                    <span class="text-2xl">Zero.</span>
                </p>
            </div>
        </div>

        <!-- Second Example -->
        <div class="max-w-6xl mx-auto mb-12">
            <div class="bg-white border-brutal p-6">
                <p class="text-lg font-urbanist font-bold text-gray-800">
                    ⭐⭐ Customer Review: "Ordered chicken tikka, received chicken korma instead."
                </p>
            </div>
        </div>

        <div class="grid md:grid-cols-3 gap-6 max-w-6xl mx-auto">
            
            <!-- BOX 1 - Total Ignore -->
            <div class="relative">
                <div class="bg-gray-300 border-4 border-gray-500 p-6 opacity-60 min-h-[300px] flex flex-col">
                    <div class="absolute -top-4 left-4 bg-red-700 text-white px-4 py-2 font-urbanist font-black text-xs">
                        ❌ USELESS
                    </div>
                    <div class="mt-8 flex-1 flex items-center justify-center">
                        <div class="text-center">
                            <p class="text-6xl mb-4">🦗</p>
                            <p class="text-2xl font-urbanist font-black text-gray-600">
                                *SILENCE*
                            </p>
                            <p class="text-sm text-gray-600 mt-4">
                                Can't be bothered
                            </p>
                        </div>
                    </div>
                    <div class="mt-4 pt-4 border-t-2 border-gray-500">
                        <p class="text-xs text-gray-700 font-bold">
                            ✗ Issue: Not addressed<br>
                            ✗ Customer: Still angry<br>
                            ✗ Outcome: Lost forever
                        </p>
                    </div>
                </div>
            </div>

            <!-- BOX 2 - Generic Rubbish -->
            <div class="relative">
                <div class="bg-gray-300 border-4 border-gray-500 p-6 opacity-60 min-h-[300px] flex flex-col">
                    <div class="absolute -top-4 left-4 bg-red-700 text-white px-4 py-2 font-urbanist font-black text-xs">
                        ❌ EQUALLY USELESS
                    </div>
                    <div class="mt-8 flex-1">
                        <div class="bg-white p-4 border-2 border-gray-500">
                            <p class="text-sm text-gray-700 italic">
                                "We appreciate your review and take all feedback seriously. We're always working to improve. Thank you for choosing us!"
                            </p>
                        </div>
                    </div>
                    <div class="mt-4 pt-4 border-t-2 border-gray-500">
                        <p class="text-xs text-gray-700 font-bold">
                            ✗ Issue: Not addressed<br>
                            ✗ Customer: Still angry<br>
                            ✗ Outcome: Lost forever
                        </p>
                    </div>
                </div>
            </div>

            <!-- BOX 3 - MeteorStrike -->
            <div class="relative">
                <div class="bg-secondary border-brutal p-6 shadow-brutal min-h-[300px] flex flex-col">
                    <div class="absolute -top-4 left-4 bg-primary text-accent px-4 py-2 font-urbanist font-black text-xs border-2 border-primary">
                        ✓ ACTUALLY USEFUL
                    </div>
                    <div class="mt-8 flex-1">
                        <div class="bg-accent p-4 border-4 border-primary">
                            <p class="text-sm text-primary font-medium">
                                "That's our mistake - wrong dish completely is not on. We've retrained kitchen staff on checking orders before they go out. Use code SORRYMATE for 20% off next time, and if we mess up again, full refund no questions."
                            </p>
                        </div>
                    </div>
                    <div class="mt-4 pt-4 border-t-4 border-primary">
                        <p class="text-xs font-bold">
                            ✓ Issue: Acknowledged & fixed<br>
                            ✓ Customer: Feels heard<br>
                            ✓ Outcome: Second chance earned
                        </p>
                    </div>
                </div>
            </div>

        </div>

        <!-- Final Punch -->
        <div class="max-w-6xl mx-auto mt-8">
            <div class="bg-red-100 border-4 border-red-700 p-6 text-center">
                <p class="text-xl font-urbanist font-black text-red-900">
                    A template response is just <span class="text-2xl">SILENT IGNORING WITH EXTRA STEPS.</span><br>
                    Same result. Same damage. Same lost customer.
                </p>
            </div>
        </div>

        <!-- Call to Action -->
        <div class="text-center mt-16">
            <p class="text-2xl font-urbanist font-black mb-6">
                Which restaurant would YOU order from again?
            </p>
            <a href="#calculator" class="inline-block bg-primary text-accent px-8 py-4 font-urbanist font-black text-xl border-brutal shadow-brutal hover:translate-x-1 hover:translate-y-1 hover:shadow-none transition-all">
                SEE WHAT IT'S COSTING YOU →
            </a>
        </div>
    </div>
</section>
Drop that in after your "Tick Tock" section.

The CTA at the bottom links to #calculator - so next we need to build the calculator section.

Ready for that?

ok so whats the codee strart to ibush

Right, here's the calculator section code to drop in after the comparison section:

html
<!-- Calculator Section -->
<section id="calculator" class="min-h-screen flex items-center justify-center bg-secondary text-primary py-20">
    <div class="container mx-auto px-6">
        <div class="text-center mb-12">
            <div class="bg-accent border-brutal p-8 mb-8 inline-block">
                <h2 class="text-5xl md:text-7xl font-urbanist font-black text-highlight">
                    SHOW ME THE DAMAGE
                </h2>
            </div>
            <p class="text-2xl md:text-3xl font-urbanist font-bold max-w-3xl mx-auto">
                Let's work out exactly how much money you're pissing away every month by ignoring reviews.
            </p>
        </div>

        <div class="max-w-3xl mx-auto bg-accent border-brutal p-8 md:p-12">
            <!-- Calculator Inputs -->
            <div class="space-y-6 mb-8">
                <div>
                    <label class="block text-xl font-urbanist font-black mb-3">
                        How many 1-2 star reviews do you get per month?
                    </label>
                    <input type="number" 
                           id="badReviews" 
                           class="w-full p-4 text-2xl font-bold text-accent border-4 border-black"
                           placeholder="e.g. 5"
                           min="0"
                           value="5">
                </div>

                <div>
                    <label class="block text-xl font-urbanist font-black mb-3">
                        What's your average order value? (£)
                    </label>
                    <input type="number" 
                           id="orderValue" 
                           class="w-full p-4 text-2xl font-bold text-accent border-4 border-black"
                           placeholder="e.g. 15"
                           min="0"
                           value="15">
                </div>

                <div>
                    <label class="block text-xl font-urbanist font-black mb-3">
                        What % of bad reviews do you currently respond to?
                    </label>
                    <input type="number" 
                           id="responseRate" 
                           class="w-full p-4 text-2xl font-bold text-accent border-4 border-black"
                           placeholder="e.g. 20"
                           min="0"
                           max="100"
                           value="20">
                    <p class="text-sm mt-2 opacity-80">Be honest. We both know it's low.</p>
                </div>
            </div>

            <button onclick="calculateDamage()" 
                    class="w-full bg-highlight text-accent font-urbanist font-black text-2xl md:text-3xl py-6 border-4 border-black shake-on-hover mb-8">
                CALCULATE MY LOSSES 💸
            </button>

            <!-- Results (hidden initially) -->
            <div id="results" class="hidden">
                <div class="bg-red-600 border-4 border-black p-8 mb-6">
                    <p class="text-xl font-bold mb-2">YOU'RE LOSING APPROXIMATELY:</p>
                    <p class="text-6xl md:text-7xl font-urbanist font-black text-highlight" id="monthlyLoss">
                        £0
                    </p>
                    <p class="text-2xl font-bold mt-2">PER MONTH</p>
                </div>

                <div class="bg-primary text-accent border-4 border-black p-6 mb-6">
                    <p class="text-lg font-bold mb-4">Here's the breakdown:</p>
                    <ul class="text-left space-y-3 text-lg">
                        <li>• <span id="ignoredReviews" class="font-black">0</span> reviews ignored per month</li>
                        <li>• Each angry customer tells <span class="font-black">15 people</span></li>
                        <li>• That's <span id="lostCustomers" class="font-black">0</span> potential customers gone</li>
                        <li>• At £<span id="avgOrder" class="font-black">0</span> per order = <span id="totalLoss" class="font-black">£0</span> lost</li>
                    </ul>
                </div>

                <div class="bg-highlight text-accent border-4 border-black p-8 text-center">
                    <p class="text-3xl font-urbanist font-black mb-4">
                        THAT'S £<span id="yearlyLoss">0</span> PER YEAR
                    </p>
                    <p class="text-xl font-bold">
                        Fix it for £49/month
                    </p>
                </div>

                <a href="#pricing" 
                   class="block w-full bg-secondary hover:bg-primary text-primary hover:text-accent font-urbanist font-black text-2xl md:text-3xl py-6 border-4 border-black text-center mt-8 transition-all">
                    STOP LOSING MONEY →
                </a>
            </div>
        </div>
    </div>
</section>

<script>
function calculateDamage() {
    // Get input values
    const badReviews = parseFloat(document.getElementById('badReviews').value) || 0;
    const orderValue = parseFloat(document.getElementById('orderValue').value) || 0;
    const responseRate = parseFloat(document.getElementById('responseRate').value) || 0;
    
    // Calculate ignored reviews
    const ignoredReviews = badReviews * (1 - (responseRate / 100));
    
    // Each ignored review = 15 lost customers
    const lostCustomers = Math.round(ignoredReviews * 15);
    
    // Calculate monthly loss
    const monthlyLoss = Math.round(lostCustomers * orderValue);
    
    // Calculate yearly loss
    const yearlyLoss = monthlyLoss * 12;
    
    // Update the results
    document.getElementById('monthlyLoss').textContent = '£' + monthlyLoss.toLocaleString();
    document.getElementById('ignoredReviews').textContent = Math.round(ignoredReviews);
    document.getElementById('lostCustomers').textContent = lostCustomers.toLocaleString();
    document.getElementById('avgOrder').textContent = orderValue;
    document.getElementById('totalLoss').textContent = '£' + monthlyLoss.toLocaleString();
    document.getElementById('yearlyLoss').textContent = yearlyLoss.toLocaleString();
    
    // Show results
    document.getElementById('results').classList.remove('hidden');
    
    // Scroll to results
    document.getElementById('results').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Allow Enter key to trigger calculation
document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('#badReviews, #orderValue, #responseRate');
    inputs.forEach(input => {
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                calculateDamage();
            }
        });
    });
});
</script>
What this does:

Three simple inputs:
Bad reviews per month
Average order value
Current response rate (be honest!)
Calculates:
Ignored reviews = bad reviews × (1 - response rate)
Lost customers = ignored reviews × 15
Monthly loss = lost customers × order value
Yearly loss = monthly × 12
Shows them:
Big scary monthly number
Breakdown of the maths
Yearly total (even scarier)
Your £49/month price (looks tiny in comparison)
CTA: Links to pricing section
Drop this in after the comparison section, then we can build the pricing section next.

Ready?

yes

Right, here's the pricing section to drop in after the calculator:

html
<!-- Pricing Section -->
<section id="pricing" class="min-h-screen flex items-center justify-center bg-accent text-primary py-20">
    <div class="container mx-auto px-6">
        <div class="text-center mb-16">
            <div class="bg-secondary border-brutal p-8 mb-8 inline-block">
                <h2 class="text-5xl md:text-7xl font-urbanist font-black text-primary">
                    STOP THE DAMAGE
                </h2>
            </div>
            <p class="text-2xl md:text-3xl font-urbanist font-bold max-w-3xl mx-auto mb-4">
                You've seen what ignoring reviews costs you.
            </p>
            <p class="text-xl md:text-2xl max-w-3xl mx-auto">
                Now see what it costs to fix it.
            </p>
        </div>

        <!-- Single Pricing Card -->
        <div class="max-w-2xl mx-auto">
            <div class="bg-secondary border-brutal p-8 md:p-12 shadow-brutal">
                <div class="text-center mb-8">
                    <h3 class="text-4xl md:text-5xl font-urbanist font-black text-primary mb-4">
                        METEORSTRIKE
                    </h3>
                    <p class="text-xl text-primary/90 mb-6">
                        Every review. Every time. Done properly.
                    </p>
                    <div class="bg-accent border-4 border-black p-6 inline-block">
                        <p class="text-6xl md:text-7xl font-urbanist font-black text-highlight">
                            £49
                        </p>
                        <p class="text-2xl font-bold text-primary">per month</p>
                    </div>
                </div>

                <div class="bg-accent border-4 border-black p-8 mb-8">
                    <p class="text-2xl font-urbanist font-black mb-6 text-center">
                        WHAT YOU GET:
                    </p>
                    <ul class="space-y-4 text-lg">
                        <li class="flex items-start">
                            <span class="text-highlight text-2xl mr-3">✓</span>
                            <span><strong class="font-black">24/7 monitoring</strong> of all your review platforms</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-highlight text-2xl mr-3">✓</span>
                            <span><strong class="font-black">Professional responses</strong> to every single review (good or bad)</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-highlight text-2xl mr-3">✓</span>
                            <span><strong class="font-black">Your brand voice</strong> - we match your tone, not some corporate template</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-highlight text-2xl mr-3">✓</span>
                            <span><strong class="font-black">Response within 24 hours</strong> - no more awkward week-old ignored reviews</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-highlight text-2xl mr-3">✓</span>
                            <span><strong class="font-black">Zero effort from you</strong> - we handle it all, you just watch your reputation improve</span>
                        </li>
                    </ul>
                </div>

                <div class="bg-highlight text-accent border-4 border-black p-6 text-center mb-8">
                    <p class="text-xl font-black">
                        That's roughly <span class="text-3xl">£1.63 per day</span>
                    </p>
                    <p class="text-lg font-bold mt-2">
                        Less than a coffee. More valuable than your entire marketing budget.
                    </p>
                </div>

                <a href="mailto:hello@meteorstrike.co.uk?subject=Sign%20Me%20Up" 
                   class="block w-full bg-accent hover:bg-primary text-highlight hover:text-accent font-urbanist font-black text-2xl md:text-3xl py-6 border-4 border-black text-center transition-all shake-on-hover">
                    GET STARTED NOW →
                </a>

                <p class="text-center text-sm mt-6 text-primary/80">
                    No contract. Cancel anytime. But you won't want to.
                </p>
            </div>
        </div>

        <!-- Social Proof / Trust Section -->
        <div class="max-w-4xl mx-auto mt-16 grid md:grid-cols-3 gap-6">
            <div class="bg-primary text-accent border-brutal p-6 text-center">
                <p class="text-4xl font-urbanist font-black mb-2">24/7</p>
                <p class="font-bold">Monitoring & Response</p>
            </div>
            <div class="bg-primary text-accent border-brutal p-6 text-center">
                <p class="text-4xl font-urbanist font-black mb-2">100%</p>
                <p class="font-bold">UK-Based Service</p>
            </div>
            <div class="bg-primary text-accent border-brutal p-6 text-center">
                <p class="text-4xl font-urbanist font-black mb-2">0</p>
                <p class="font-bold">Corporate Waffle</p>
            </div>
        </div>
    </div>
</section>



FAQs SECTION
html
<!-- FAQs Section -->
<section id="faqs" class="min-h-screen flex items-center justify-center bg-primary text-accent py-20">
    <div class="container mx-auto px-6">
        <div class="text-center mb-16">
            <div class="bg-secondary border-brutal p-8 mb-8 inline-block">
                <h2 class="text-5xl md:text-7xl font-urbanist font-black text-primary">
                    QUESTIONS?
                </h2>
            </div>
            <p class="text-2xl md:text-3xl font-urbanist font-bold max-w-3xl mx-auto">
                Here's everything you need to know. No waffle.
            </p>
        </div>

        <div class="max-w-4xl mx-auto space-y-6">
            
            <!-- FAQ 1 -->
            <div class="bg-accent border-brutal p-6 md:p-8">
                <h3 class="text-2xl md:text-3xl font-urbanist font-black text-secondary mb-4">
                    How does it work?
                </h3>
                <p class="text-lg md:text-xl leading-relaxed">
                    We monitor all your review platforms 24/7. When a review comes in, we write a professional response in your voice and post it within 24 hours. You approve nothing, you do nothing. It just happens.
                </p>
            </div>

            <!-- FAQ 2 -->
            <div class="bg-accent border-brutal p-6 md:p-8">
                <h3 class="text-2xl md:text-3xl font-urbanist font-black text-secondary mb-4">
                    What platforms do you cover?
                </h3>
                <p class="text-lg md:text-xl leading-relaxed">
                    Google, Just Eat, Deliveroo, Uber Eats, Tripadvisor. Basically anywhere customers can leave you reviews.
                </p>
            </div>

            <!-- FAQ 3 -->
            <div class="bg-accent border-brutal p-6 md:p-8">
                <h3 class="text-2xl md:text-3xl font-urbanist font-black text-secondary mb-4">
                    Will the responses sound like a robot?
                </h3>
                <p class="text-lg md:text-xl leading-relaxed">
                    No. We match your brand voice. If you're friendly, we're friendly. If you're professional, we're professional. If you swear at customers... we probably won't do that, but you get the idea.
                </p>
            </div>

            <!-- FAQ 4 -->
            <div class="bg-accent border-brutal p-6 md:p-8">
                <h3 class="text-2xl md:text-3xl font-urbanist font-black text-secondary mb-4">
                    What if I don't like a response?
                </h3>
                <p class="text-lg md:text-xl leading-relaxed">
                    Tell us and we'll change it. Simple as that. We get it right 99% of the time, but if we don't, we fix it immediately.
                </p>
            </div>

            <!-- FAQ 5 -->
            <div class="bg-accent border-brutal p-6 md:p-8">
                <h3 class="text-2xl md:text-3xl font-urbanist font-black text-secondary mb-4">
                    Is there a contract?
                </h3>
                <p class="text-lg md:text-xl leading-relaxed">
                    No. Cancel anytime. No notice period. No bollocks. If you don't like it, stop paying. We're confident you won't want to.
                </p>
            </div>

            <!-- FAQ 6 -->
            <div class="bg-accent border-brutal p-6 md:p-8">
                <h3 class="text-2xl md:text-3xl font-urbanist font-black text-secondary mb-4">
                    How quickly can you start?
                </h3>
                <p class="text-lg md:text-xl leading-relaxed">
                    Sign up today, we start tomorrow. Onboarding takes 10 minutes. First responses go out within 24 hours.
                </p>
            </div>

            <!-- FAQ 7 -->
            <div class="bg-accent border-brutal p-6 md:p-8">
                <h3 class="text-2xl md:text-3xl font-urbanist font-black text-secondary mb-4">
                    Do you speak Urdu?
                </h3>
                <p class="text-lg md:text-xl leading-relaxed">
                    Yes. We can help non-English speaking owners get set up and understand what we're doing. Your customers get English responses, you get support in your language.
                </p>
            </div>

            <!-- FAQ 8 -->
            <div class="bg-accent border-brutal p-6 md:p-8">
                <h3 class="text-2xl md:text-3xl font-urbanist font-black text-secondary mb-4">
                    What if I get a terrible review?
                </h3>
                <p class="text-lg md:text-xl leading-relaxed">
                    We handle it professionally. We acknowledge the issue, explain what you're doing to fix it, and offer to make it right. We turn angry customers into second chances.
                </p>
            </div>

            <!-- FAQ 9 -->
            <div class="bg-accent border-brutal p-6 md:p-8">
                <h3 class="text-2xl md:text-3xl font-urbanist font-black text-secondary mb-4">
                    Why are you so cheap compared to others?
                </h3>
                <p class="text-lg md:text-xl leading-relaxed">
                    Because we're not paying for fancy London offices, account managers who talk waffle, or sales teams on commission. We're automated where it matters, human where it matters. That's it.
                </p>
            </div>

        </div>

        <div class="text-center mt-16">
            <p class="text-xl md:text-2xl font-bold mb-6">
                Still got questions? Just ask.
            </p>
            <a href="mailto:hello@meteorstrike.co.uk" 
               class="inline-block bg-secondary hover:bg-highlight text-primary hover:text-accent font-urbanist font-black text-xl md:text-2xl px-8 py-4 border-brutal shadow-brutal hover:translate-x-1 hover:translate-y-1 hover:shadow-none transition-all">
                EMAIL US →
            </a>
        </div>
    </div>
</section>
FINAL WARNING SECTION
html
<!-- Final Warning Section -->
<section class="min-h-screen flex items-center justify-center bg-gray-900 text-primary py-20 relative overflow-hidden">
    <div class="absolute inset-0 bg-black opacity-90"></div>
    <div class="container mx-auto px-6 text-center relative z-10">
        
        <div class="bg-red-600 border-brutal p-8 mb-12 inline-block pulse-warning">
            <h2 class="text-6xl md:text-8xl font-urbanist font-black text-primary text-shadow-brutal">
                LAST CHANCE
            </h2>
        </div>

        <div class="max-w-3xl mx-auto mb-12">
            <p class="text-3xl md:text-4xl font-urbanist font-black text-highlight mb-8">
                While you're reading this, your competitors are responding to reviews.
            </p>
            <p class="text-xl md:text-2xl font-bold mb-6">
                They're winning customers you should have.
            </p>
            <p class="text-xl md:text-2xl font-bold mb-6">
                They're building trust while you're silent.
            </p>
            <p class="text-xl md:text-2xl font-bold text-secondary mb-12">
                How much longer can you afford to ignore this?
            </p>
        </div>

        <div class="bg-accent border-brutal p-10 md:p-16 max-w-4xl mx-auto mb-12">
            <p class="text-2xl md:text-3xl font-urbanist font-black mb-8">
                EVERY DAY YOU WAIT:
            </p>
            <div class="space-y-4 text-left max-w-2xl mx-auto text-lg md:text-xl">
                <div class="flex items-start">
                    <span class="text-red-500 text-3xl mr-4">✗</span>
                    <span>More reviews go unanswered</span>
                </div>
                <div class="flex items-start">
                    <span class="text-red-500 text-3xl mr-4">✗</span>
                    <span>More customers choose your competitor</span>
                </div>
                <div class="flex items-start">
                    <span class="text-red-500 text-3xl mr-4">✗</span>
                    <span>More revenue walks out the door</span>
                </div>
                <div class="flex items-start">
                    <span class="text-red-500 text-3xl mr-4">✗</span>
                    <span>Your Google ranking drops further</span>
                </div>
            </div>
        </div>

        <div class="mb-12">
            <p class="text-2xl md:text-3xl font-urbanist font-black text-highlight mb-4">
                £99/month fixes all of this.
            </p>
            <p class="text-xl md:text-2xl font-bold">
                That's £3.30 per day. Less than a coffee.
            </p>
        </div>

        <a href="#pricing" 
           class="inline-block bg-highlight hover:bg-secondary text-accent font-urbanist font-black text-3xl md:text-4xl px-12 py-6 border-brutal shadow-brutal shake-on-hover mb-8">
            STOP LOSING CUSTOMERS NOW →
        </a>

        <p class="text-lg text-primary/80 mt-8">
            Or keep ignoring reviews and watch your business slowly die. Your choice.
        </p>
    </div>
</section>

<!-- Pricing Section -->
<section id="pricing" class="min-h-screen flex items-center justify-center bg-accent text-primary py-20">
    <div class="container mx-auto px-6">
        <div class="text-center mb-16">
            <div class="bg-secondary border-brutal p-8 mb-8 inline-block">
                <h2 class="text-5xl md:text-7xl font-urbanist font-black text-primary">
                    STOP THE DAMAGE
                </h2>
            </div>
            <p class="text-2xl md:text-3xl font-urbanist font-bold max-w-3xl mx-auto mb-4">
                You've seen what ignoring reviews costs you.
            </p>
            <p class="text-xl md:text-2xl max-w-3xl mx-auto">
                Now see what it costs to fix it.
            </p>
        </div>

        <!-- Single Pricing Card with Intro Offer -->
        <div class="max-w-2xl mx-auto">
            <div class="bg-secondary border-brutal p-8 md:p-12 shadow-brutal relative">
                
                <!-- Intro Offer Badge -->
                <div class="absolute -top-6 left-1/2 transform -translate-x-1/2">
                    <div class="bg-highlight text-accent px-6 py-3 border-4 border-black font-urbanist font-black text-lg animate-pulse">
                        ⚡ INTRO OFFER - FIRST 100 CUSTOMERS
                    </div>
                </div>

                <div class="text-center mb-8 mt-8">
                    <h3 class="text-4xl md:text-5xl font-urbanist font-black text-primary mb-4">
                        METEORSTRIKE
                    </h3>
                    <p class="text-xl text-primary/90 mb-6">
                        Every review. Every time. Done properly.
                    </p>
                    
                    <!-- Price with Strikethrough -->
                    <div class="mb-4">
                        <p class="text-2xl text-primary/60 line-through mb-2">
                            Normal price: £79/month
                        </p>
                    </div>

                    <div class="bg-accent border-4 border-black p-6 inline-block">
                        <p class="text-6xl md:text-7xl font-urbanist font-black text-highlight">
                            £49
                        </p>
                        <p class="text-2xl font-bold text-primary">per month</p>
                        <p class="text-lg text-highlight font-black mt-2">
                            LOCKED IN FOREVER
                        </p>
                    </div>
                </div>

                <div class="bg-accent border-4 border-black p-8 mb-8">
                    <p class="text-2xl font-urbanist font-black mb-6 text-center">
                        WHAT YOU GET:
                    </p>
                    <ul class="space-y-4 text-lg">
                        <li class="flex items-start">
                            <span class="text-highlight text-2xl mr-3">✓</span>
                            <span><strong class="font-black">24/7 monitoring</strong> of all your review platforms (Google, Just Eat, Deliveroo, Uber Eats)</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-highlight text-2xl mr-3">✓</span>
                            <span><strong class="font-black">Professional responses</strong> to every single review (good or bad)</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-highlight text-2xl mr-3">✓</span>
                            <span><strong class="font-black">Your brand voice</strong> - we match your tone, not some corporate template</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-highlight text-2xl mr-3">✓</span>
                            <span><strong class="font-black">Response within 24 hours</strong> - no more awkward week-old ignored reviews</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-highlight text-2xl mr-3">✓</span>
                            <span><strong class="font-black">Zero effort from you</strong> - we handle it all, you just watch your reputation improve</span>
                        </li>
                    </ul>
                </div>

                <div class="bg-highlight text-accent border-4 border-black p-6 text-center mb-8">
                    <p class="text-xl font-black mb-2">
                        That's roughly <span class="text-3xl">£1.63 per day</span>
                    </p>
                    <p class="text-lg font-bold">
                        Less than a coffee. More valuable than your entire marketing budget.
                    </p>
                    <p class="text-sm font-bold mt-4 text-red-700">
                        Price goes up to £79/month after first 100 customers
                    </p>
                </div>

                <a href="mailto:hello@meteorstrike.co.uk?subject=Sign%20Me%20Up%20-%20Intro%20Offer" 
                   class="block w-full bg-accent hover:bg-primary text-highlight hover:text-accent font-urbanist font-black text-2xl md:text-3xl py-6 border-4 border-black text-center transition-all shake-on-hover">
                    LOCK IN £49/MONTH FOREVER →
                </a>

                <p class="text-center text-sm mt-6 text-primary/80">
                    No contract. Cancel anytime. But you won't want to.
                </p>
            </div>
        </div>

        <!-- Scarcity Counter (Optional - can add later) -->
        <div class="max-w-2xl mx-auto mt-8 text-center">
            <div class="bg-red-600 border-4 border-black p-4 inline-block">
                <p class="text-xl font-urbanist font-black text-primary">
                    ⏰ 87 INTRO SPOTS LEFT
                </p>
            </div>
            <p class="text-sm text-primary/70 mt-2">
                (You can update this number manually as you get customers)
            </p>
        </div>

        <!-- Trust Section -->
        <div class="max-w-4xl mx-auto mt-16 grid md:grid-cols-3 gap-6">
            <div class="bg-primary text-accent border-brutal p-6 text-center">
                <p class="text-4xl font-urbanist font-black mb-2">24/7</p>
                <p class="font-bold">Monitoring & Response</p>
            </div>
            <div class="bg-primary text-accent border-brutal p-6 text-center">
                <p class="text-4xl font-urbanist font-black mb-2">100%</p>
                <p class="font-bold">UK-Based Service</p>
            </div>
            <div class="bg-primary text-accent border-brutal p-6 text-center">
                <p class="text-4xl font-urbanist font-black mb-2">0</p>
                <p class="font-bold">Corporate Waffle</p>
            </div>
        </div>
    </div>
</section>
