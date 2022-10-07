<?php
class Rumus
{
    public function __construct($panjang, $lebar, $satuan)
    {
        $this->panjang = $panjang;
        $this->lebar = $lebar;
        $this->satuan = $satuan;
    }

    public function getLuas()
    {
        return "Luas: " . $this->panjang * $this->lebar . " $this->satuan";
    }

    public function getKeliling()
    {
        return "Keliling: " . 2 * ($this->panjang + $this->lebar) . " $this->satuan";
    }
}

class PersegiPanjang extends Rumus
{
    public function cetakLuas()
    {
        return $this->getLuas();
    }

    public function cetakKeliling()
    {
        return $this->getKeliling();
    }
}

$persegiPanjang = new PersegiPanjang(10, 20, "cm");

echo "Hasilnya";
echo "<br><br>";

echo $persegiPanjang->cetakLuas();
echo "<br>";
echo $persegiPanjang->cetakKeliling();
