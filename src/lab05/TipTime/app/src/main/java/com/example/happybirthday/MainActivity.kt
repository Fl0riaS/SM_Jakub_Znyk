package com.example.happybirthday

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.happybirthday.databinding.ActivityMainBinding
import java.text.NumberFormat

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.calculateButton.setOnClickListener { calculateTip() }
    }

    private fun calculateTip() {
        // Get written cost
        val cost = binding.costOfService.text.toString().toDoubleOrNull()

        if (cost == null) {
            binding.tipResult.text = ""
            return
        }

        // Get chosen tip percentage
        val tipPercentage = when (binding.tipOptions.checkedRadioButtonId) {
            R.id.option_twenty_percent -> 0.20
            R.id.option_eighteen_percent -> 0.18
            else -> 0.15
        }

        // Calculate tip
        var tip = tipPercentage * cost

        // Round tip if switch is checked
        if(binding.roundUpSwitch.isChecked) {
            tip = kotlin.math.ceil(tip)
        }

        // Format tip in order to show it in proper currency
        val formattedTip = NumberFormat.getCurrencyInstance().format(tip)

        // Set text in view
        binding.tipResult.text = getString(R.string.tip_amount, formattedTip)
    }
}
