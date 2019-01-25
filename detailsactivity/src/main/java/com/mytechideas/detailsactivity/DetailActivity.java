package com.mytechideas.detailsactivity;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class DetailActivity extends AppCompatActivity {

    public static final String JOKE_STRING= "joke";

    private TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);


        Intent intent=getIntent();

        if(intent.hasExtra(JOKE_STRING)){
        textView=(TextView) findViewById(R.id.displayView);
        textView.setText(intent.getStringExtra(JOKE_STRING));

        }
    }
}
