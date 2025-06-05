def calc_band_length(L_load, wishbone, stretch, knot=0.5, muzzle_hole=2):
    L_eff = L_load - wishbone - knot
    L_band = 2 * ((L_eff / stretch) + knot) + muzzle_hole
    return round(L_band, 2)

def calc_band_stretch(L_load, wishbone, L_band, knot=0.5, muzzle_hole=2):
    L_eff = L_load - wishbone - knot
    stretch = L_eff * (1 / (((L_band - muzzle_hole) / 2) - knot))
    return int(round(stretch, 2) * 100)