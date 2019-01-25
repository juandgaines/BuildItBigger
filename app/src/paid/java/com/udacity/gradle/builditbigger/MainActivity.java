package com.udacity.gradle.builditbigger;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;

import com.mytechideas.detailsactivity.DetailActivity;


public class MainActivity extends AppCompatActivity implements EndpointsAsyncTask.AsyncResponse {

    private static final String JOKE_STRING= "joke";



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();


        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void tellJoke(View view) {
        new EndpointsAsyncTask().execute(this);

        //Toast.makeText(this, joker.getJoke(), Toast.LENGTH_SHORT).show();
    }


    @Override
    public void processFinish(String output) {

        Intent intent = new Intent(this,DetailActivity.class);
        intent.putExtra(JOKE_STRING,output);
        startActivity(intent);
    }
}
