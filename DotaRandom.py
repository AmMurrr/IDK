import random
Spi=['Aghanims Shard',"Null Talisman",
     "Magic Wand","Helm of the Overlord",'Wraith Band',"Falcon Blade",
     "Orb of Corrosion","Soul Ring","Bracer",'Moon Shard','Boots of Travel',
     'Helm of the Dominator','Hand of Midas','Mask of Madness','Perseverance',
     'Oblivion Staff','Phase Boots','Power Treads','Orchid Malevolence',
     'Solar Crest','Aghanims Scepter','Refresher Orb','Vladmirs Offering','Holy Locket'
     'Octarine Core','Scythe of Vyse','Gleipnir','Wind Waker','Dagon',
     'Veil of Discord','Glimmer Cape','Force Staff','Aether Lens','Mekansm',
     'Drum of Endurance','Arcane Boots','Medallion of Courage',
     'Tranquil Boots','Revenants Brooch','Abyssal Blade','Bloodthorn',
     'Divine Rapier','Divine Rapier','Divine Rapier','Silver Edge',
     'Daedalus','Radiance','Butterfly','Monkey King Bar','Monkey King Bar',
     'Nullifier','Ethereal Blade','Battle Fury','Desolator','Shadow Blade',
     'Skull Basher','Armlet of Mordiggian','Meteor Hammer','Crystalys'
     'Urn of Shadows','Headdress','Ring of Basilius','Buckler',
     'Witch Blade','Euls Scepter of Divinity','Rod of Atos',
     "Boots of Travel 2",'Bloodstone','Assault Cuirass','Heart of Tarrasque',
     'Shivas Guard','Linkens Sphere','Manta Style','Hurricane Pike',
     'Black King Bar','Lotus Orb','Crimson Guard','Eternal Shroud',
     'Soul Booster','Aeon Disk','Blade Mail','Vanguard','Hood of Defiance',
     'Arcane Blink','Swift Blink','Overwhelming Blink','Mjollnir',
     'Eye of Skadi','Satanic','Yasha and Kaya','Sange and Yasha',
     'Kaya and Sange','Heavens Halberd','Mage Slayer',
     'Diffusal Blade','Maelstrom','Echo Sabre','Kaya','Yasha','Sange',
     'Dragon Lance']
x=input()
while x!='z':
    ran=random.randint(0,len(Spi)-1)
    print(Spi[ran])
    x=input()
