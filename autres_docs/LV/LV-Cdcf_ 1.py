"""

Auteur: 
Nom du projet: LV-Cdcf_ 1
Description: Commande combinatoire de la vitre du coté chauffeur :

Lorsque le chauffeur soulève le bouton de commande (entrée bpmc) cela doit provoquer la montée (sortie M) de la vitre par l’intermédiaire d’un motoréducteur, et lorsqu’il appuie sur ce même bouton (entrée bpdc) cela doit provoquer la descente (sortie D) de la vitre.

La montée comme la descente doivent s’arrêter lorsque la vitre arrive en fin de course (entrée fdc).
Mode: vittascience
Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><variables><variable id=".h#({A@=):vO`Ngs;q2W">bpmc</variable><variable id="nw;PK9UW1OAa]4f-Wg85">bpdc</variable><variable id="-1WQ4IO3yp)=+Md=^wu]">fdc</variable></variables><block type="forever" id="o[WN]+eeF.OUxGch67@8" x="-1012" y="-1413"><statement name="DO"><block type="variables_set" id="$1G=26X~(X}pU4RXk{=h"><field name="VAR" id=".h#({A@=):vO`Ngs;q2W">bpmc</field><value name="VALUE"><shadow type="text" id="L7PV+5NE@bqoHlbN7Qf6"><field name="TEXT"></field></shadow><block type="io_readDigitalPin" id="T!uo|mXb|BXtyo6=T:^4"><field name="PIN">pin5</field></block></value><next><block type="variables_set" id="sj-*x.i2J/v_~4Vk4%E{"><field name="VAR" id="nw;PK9UW1OAa]4f-Wg85">bpdc</field><value name="VALUE"><shadow type="text" id="xhCt?Y9{^h:iC%Xzt%e-"><field name="TEXT"></field></shadow><block type="io_readDigitalPin" id="dnsL?Pma}U(;h?ze|4Az"><field name="PIN">pin11</field></block></value><next><block type="variables_set" id="_N%N%ZjF3B.Ru=@PZSLz"><field name="VAR" id="-1WQ4IO3yp)=+Md=^wu]">fdc</field><value name="VALUE"><shadow type="text" id="Xqs-v!o-RgQ*!FvQ;K.-"><field name="TEXT"></field></shadow><block type="io_readDigitalPin" id="[DYVY!i5c.kSZcoA|Q_x"><field name="PIN">pin1</field></block></value><next><block type="controls_if" id="K!UJc@V_[9S`:Moy|0L3"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="logic_operation" id="AJ7Sj*|IVqKC678xs4ss"><field name="OP">AND</field><value name="A"><block type="variables_get" id="i2A4z#Y5?{Hgzxc4|*Y4"><field name="VAR" id=".h#({A@=):vO`Ngs;q2W">bpmc</field></block></value><value name="B"><block type="logic_operation" id="*v;:iA7l-iJ6=RtGkIb5"><field name="OP">AND</field><value name="A"><block type="logic_negate" id="zPNlx%W(zSYf?:2cG?f8"><value name="BOOL"><block type="variables_get" id="?kZu67CTeg*@5:=$b+8:"><field name="VAR" id="nw;PK9UW1OAa]4f-Wg85">bpdc</field></block></value></block></value><value name="B"><block type="logic_negate" id="XmI{+isMo9QHpbTN(?U5"><value name="BOOL"><block type="variables_get" id="7S[aHu+UA-y7q-@rM3W!"><field name="VAR" id="-1WQ4IO3yp)=+Md=^wu]">fdc</field></block></value></block></value></block></value></block></value><statement name="DO0"><block type="show_leds" id="xhCs^novhc?DMTs#~#EU"><field name="LED00">FALSE</field><field name="LED01">FALSE</field><field name="LED02">TRUE</field><field name="LED03">FALSE</field><field name="LED04">FALSE</field><field name="LED10">FALSE</field><field name="LED11">TRUE</field><field name="LED12">TRUE</field><field name="LED13">TRUE</field><field name="LED14">FALSE</field><field name="LED20">TRUE</field><field name="LED21">FALSE</field><field name="LED22">TRUE</field><field name="LED23">FALSE</field><field name="LED24">TRUE</field><field name="LED30">FALSE</field><field name="LED31">FALSE</field><field name="LED32">TRUE</field><field name="LED33">FALSE</field><field name="LED34">FALSE</field><field name="LED40">FALSE</field><field name="LED41">FALSE</field><field name="LED42">TRUE</field><field name="LED43">FALSE</field><field name="LED44">FALSE</field></block></statement><value name="IF1"><block type="logic_operation" id="?rv_G6hdRKyTc8DSo%WL"><field name="OP">AND</field><value name="A"><block type="variables_get" id="@SqP^x]f0bp]KXG5:sGS"><field name="VAR" id="nw;PK9UW1OAa]4f-Wg85">bpdc</field></block></value><value name="B"><block type="logic_operation" id="7iNeEQ{mlx3j219}HBNX"><field name="OP">AND</field><value name="A"><block type="logic_negate" id="b=P@s%izE1Q6DwFRko7{"><value name="BOOL"><block type="variables_get" id="Cj-hh`^-kBpZD#l^]*$a"><field name="VAR" id=".h#({A@=):vO`Ngs;q2W">bpmc</field></block></value></block></value><value name="B"><block type="logic_negate" id="-y`$oMZQITBlp.pNgS9r"><value name="BOOL"><block type="variables_get" id="-v[,8=VlGAi=*UNRf(Q_"><field name="VAR" id="-1WQ4IO3yp)=+Md=^wu]">fdc</field></block></value></block></value></block></value></block></value><statement name="DO1"><block type="show_leds" id="_EZ_LmLbHKdY}M}+nW(V"><field name="LED00">FALSE</field><field name="LED01">FALSE</field><field name="LED02">TRUE</field><field name="LED03">FALSE</field><field name="LED04">FALSE</field><field name="LED10">FALSE</field><field name="LED11">FALSE</field><field name="LED12">TRUE</field><field name="LED13">FALSE</field><field name="LED14">FALSE</field><field name="LED20">TRUE</field><field name="LED21">FALSE</field><field name="LED22">TRUE</field><field name="LED23">FALSE</field><field name="LED24">TRUE</field><field name="LED30">FALSE</field><field name="LED31">TRUE</field><field name="LED32">TRUE</field><field name="LED33">TRUE</field><field name="LED34">FALSE</field><field name="LED40">FALSE</field><field name="LED41">FALSE</field><field name="LED42">TRUE</field><field name="LED43">FALSE</field><field name="LED44">FALSE</field></block></statement><statement name="ELSE"><block type="show_icon" id="}7:8;2JF;LHUOxNuVP~0"><field name="ICON">NO</field></block></statement></block></next></block></next></block></next></block></statement></block><block type="on_start" id="G[=T#8yqB70`NFgYq}GP" deletable="false" x="-237" y="-1388"></block></xml>

Projet généré par Vittascience.

Il contient le code python ainsi que le code blocs, et peut être importé
sur l'interface http://vittascience.com/microbit

"""

from microbit import *

while True:
  bpmc = pin5.read_digital()
  bpdc = pin11.read_digital()
  fdc = pin1.read_digital()
  if bpmc and not bpdc and not fdc:
    led_image = Image('00900:09990:90909:00900:00900')
    display.show(led_image)
  elif bpdc and not bpmc and not fdc:
    led_image = Image('00900:00900:90909:09990:00900')
    display.show(led_image)
  else:
    display.show(Image.NO)
