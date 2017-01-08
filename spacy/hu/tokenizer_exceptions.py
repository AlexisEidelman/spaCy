# encoding: utf8
from __future__ import unicode_literals

ABBREVIATIONS = """
AkH.
Aö.
B.CS.
B.S.
B.Sc.
B.ú.é.k.
BE.
BEK.
BSC.
BSc.
BTK.
Be.
Bek.
Bfok.
Bk.
Bp.
Btk.
Btke.
Btét.
CSC.
Cal.
Co.
Colo.
Comp.
Copr.
Cs.
Csc.
Csop.
Ctv.
D.
DR.
Dipl.
Dr.
Dsz.
Dzs.
Fla.
Főszerk.
GM.
Gy.
HKsz.
Hmvh.
Inform.
K.m.f.
KER.
KFT.
KRT.
Ker.
Kft.
Kong.
Korm.
Kr.
Kr.e.
Kr.u.
Krt.
M.A.
M.S.
M.SC.
M.Sc.
MA.
MSC.
MSc.
Mass.
Mlle.
Mme.
Mo.
Mr.
Mrs.
Ms.
Mt.
N.N.
NB.
NBr.
Nat.
Nr.
Ny.
Nyh.
Nyr.
Op.
P.H.
P.S.
PH.D.
PHD.
PROF.
Ph.D
PhD.
Pp.
Proc.
Prof.
Ptk.
Rer.
S.B.
SZOLG.
Salg.
St.
Sz.
Szfv.
Szjt.
Szolg.
Szt.
Sztv.
TEL.
Tel.
Ty.
Tyr.
Ui.
Vcs.
Vhr.
X.Y.
Zs.
a.C.
ac.
adj.
adm.
ag.
agit.
alez.
alk.
altbgy.
an.
ang.
arch.
at.
aug.
b.a.
b.s.
b.sc.
bek.
belker.
berend.
biz.
bizt.
bo.
bp.
br.
bsc.
bt.
btk.
ca.
cc.
cca.
cf.
cif.
co.
corp.
cos.
cs.
csc.
csüt.
cső.
ctv.
dbj.
dd.
ddr.
de.
dec.
dikt.
dipl.
dj.
dk.
dny.
dolg.
dr.
du.
dzs.
ea.
ed.
eff.
egyh.
ell.
elv.
elvt.
em.
eng.
eny.
et.
etc.
ev.
ezr.
eü.
f.h.
f.é.
fam.
febr.
fej.
felv.
felügy.
ff.
ffi.
fhdgy.
fil.
fiz.
fm.
foglalk.
ford.
fp.
fr.
frsz.
fszla.
fszt.
ft.
fuv.
főig.
főisk.
főtörm.
főv.
gazd.
gimn.
gk.
gkv.
gondn.
gr.
grav.
gy.
gyak.
gyártm.
gör.
hads.
hallg.
hdm.
hdp.
hds.
hg.
hiv.
hk.
hm.
ho.
honv.
hp.
hr.
hrsz.
hsz.
ht.
htb.
hv.
hőm.
i.e.
i.sz.
id.
ifj.
ig.
igh.
ill.
imp.
inc.
ind.
inform.
inic.
int.
io.
ip.
ir.
irod.
isk.
ism.
izr.
iá.
jan.
jav.
jegyz.
jjv.
jkv.
jogh.
jogt.
jr.
jvb.
júl.
jún.
karb.
kat.
kb.
kcs.
kd.
ker.
kf.
kft.
kht.
kir.
kirend.
kisip.
kiv.
kk.
kkt.
klin.
kp.
krt.
kt.
ktsg.
kult.
kv.
kve.
képv.
kísérl.
kóth.
könyvt.
körz.
köv.
közj.
közl.
közp.
közt.
kü.
lat.
ld.
legs.
lg.
lgv.
loc.
lt.
ltd.
ltp.
luth.
m.a.
m.s.
m.sc.
ma.
mat.
mb.
med.
megh.
met.
mf.
mfszt.
min.
miss.
mjr.
mjv.
mk.
mlle.
mme.
mn.
mozg.
mr.
mrs.
ms.
msc.
má.
máj.
márc.
mé.
mélt.
mü.
műh.
műsz.
műv.
művez.
nagyker.
nagys.
nat.
nb.
neg.
nk.
nov.
nu.
ny.
nyilv.
nyrt.
nyug.
obj.
okl.
okt.
olv.
orsz.
ort.
ov.
ovh.
pf.
pg.
ph.d
ph.d.
phd.
pk.
pl.
plb.
plc.
pld.
plur.
pol.
polg.
poz.
pp.
proc.
prof.
prot.
pság.
ptk.
pu.
pü.
r.k.
rac.
rad.
red.
ref.
reg.
rer.
rev.
rf.
rkp.
rkt.
rt.
rtg.
röv.
s.b.
s.k.
sa.
sel.
sgt.
sm.
st.
stat.
stb.
strat.
sz.
szakm.
szaksz.
szakszerv.
szd.
szds.
szept.
szerk.
szf.
szimf.
szjt.
szkv.
szla.
szn.
szolg.
szt.
szubj.
szöv.
szül.
tanm.
tb.
tbk.
tc.
techn.
tek.
tel.
tf.
tgk.
ti.
tip.
tisztv.
titks.
tk.
tkp.
tny.
tp.
tszf.
tszk.
tszkv.
tv.
tvr.
ty.
törv.
tü.
ua.
ui.
unit.
uo.
uv.
vas.
vb.
vegy.
vh.
vhol.
vill.
vizsg.
vk.
vkf.
vkny.
vm.
vol.
vs.
vsz.
vv.
vál.
vízv.
vö.
zrt.
zs.
Ész.
Új-Z.
ÚjZ.
á.
ált.
ápr.
ásv.
é.
ék.
ény.
érk.
évf.
í.
ó.
össz.
ötk.
özv.
ú.
úm.
ún.
út.
üag.
üd.
üdv.
üe.
ümk.
ütk.
üv.
ő.
ű.
őrgy.
őrpk.
őrv.
""".strip().split()

OTHER_EXC = """
-e
""".strip().split()
