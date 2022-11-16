import math
import Variables_for_moment_of_inertia as Var

total_area = Var.Spar_fr_len * Var.Spar_fr_th + Var.Spar_re_len * Var.Spar_re_th + Var.Sheet_bottom_len * Var.Sheet_bottom_th + Var.Sheet_top_len * Var.Sheet_top_th + Var.Str_A * Var.Str_N
Str_dis_top = Var.Sheet_top_len / ((Var.Str_N / 2) + 1)
Str_dis_bottom = Var.Sheet_bottom_len / ((Var.Str_N / 2) + 1)

z_tilda_Spar_fr = Var.Spar_fr_len / 2
z_tilda_Spar_re = (Var.Sheet_top_len) * math.sin(Var.Sheet_top_angle) + Var.Spar_re_len / 2
z_tilda_Sheet_top = (Var.Sheet_top_len / 2) * math.sin(Var.Sheet_top_angle)
z_tilda_Sheet_bottom = (Var.Spar_fr_len / 2) - ((Var.Sheet_bottom_len / 2) * math.sin(Var.Sheet_bottom_angle))

z_tilda_Str_bottom = []
for i in range(int(Var.Str_N / 2)):
    z_tilda_Str_N = Var.Spar_fr_len - (Str_dis_bottom * (i+1) * math.sin(Var.Sheet_bottom_angle))
    z_tilda_Str_bottom.append(z_tilda_Str_N)

z_tilda_Str_top = []
for i in range(int(Var.Str_N / 2)):
    z_tilda_Str_P = Str_dis_top * (i+1) * math.sin(Var.Sheet_top_angle)
    z_tilda_Str_bottom.append(z_tilda_Str_P)


Spar_fr_A = Var.Spar_fr_len*Var.Spar_fr_th
Spar_re_A = Var.Spar_re_len*Var.Spar_re_th
Sheet_top_A = Var.Sheet_top_len*Var.Sheet_top_th
Sheet_bottom_A = Var.Sheet_bottom_len*Var.Sheet_bottom_th

sum_of_products = 5

