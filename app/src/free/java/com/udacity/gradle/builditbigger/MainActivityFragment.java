package com.udacity.gradle.builditbigger;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ProgressBar;

import com.google.android.gms.ads.AdListener;
import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdView;
import com.google.android.gms.ads.InterstitialAd;
import com.mytechideas.detailsactivity.DetailActivity;
import com.udacity.gradle.builditbigger.R;


/**
 * A placeholder fragment containing a simple view.
 */
public class MainActivityFragment extends Fragment implements EndpointsAsyncTask.AsyncResponse{

    private String joke;
    private EndpointsAsyncTask asyncTask= new EndpointsAsyncTask(){
        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);
            joke=result;

        }
    };

    public MainActivityFragment() {

    }

    private InterstitialAd mInterstitial;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View root = inflater.inflate(R.layout.fragment_main, container, false);

        AdView mAdView = (AdView) root.findViewById(R.id.adView);
        Button mButton = (Button) root.findViewById(R.id.buttonAsync);

        final ProgressBar spinner;
        spinner = (ProgressBar)root.findViewById(R.id.progressBar);
        asyncTask.execute(getContext());
        mInterstitial= new InterstitialAd(getContext());
        mInterstitial.setAdListener(new AdListener() {
            @Override
            public void onAdLoaded() {
                // Code to be executed when an ad finishes loading.
            }

            @Override
            public void onAdFailedToLoad(int errorCode) {
                // Code to be executed when an ad request fails.
            }

            @Override
            public void onAdOpened() {
                // Code to be executed when the ad is displayed.
            }

            @Override
            public void onAdLeftApplication() {
                // Code to be executed when the user has left the app.
            }

            @Override
            public void onAdClosed() {
                // Code to be executed when when the interstitial ad is closed.
                Intent intent = new Intent(getContext(),DetailActivity.class);
                intent.putExtra(DetailActivity.JOKE_STRING, joke);
                spinner.setVisibility(View.INVISIBLE);
                startActivity(intent);
            }
        });

        mButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                spinner.setVisibility(View.VISIBLE);
                if (mInterstitial.isLoaded()) {
                    mInterstitial.show();

                } else {
                    Log.d("TAG", "The interstitial wasn't loaded yet.");
                }

            }
        });

        mInterstitial.setAdUnitId("ca-app-pub-3940256099942544/1033173712");
        mInterstitial.loadAd(new AdRequest.Builder().build());
        // Create an ad request. Check logcat output for the hashed device ID to
        // get test ads on a physical device. e.g.
        // "Use AdRequest.Builder.addTestDevice("ABCDEF012345") to get test ads on this device."
        AdRequest adRequest = new AdRequest.Builder()
                .addTestDevice(AdRequest.DEVICE_ID_EMULATOR)
                .build();
        mAdView.loadAd(adRequest);

        return root;
    }

    @Override
    public void processFinish(String output) {

        Intent intent = new Intent(getContext(),DetailActivity.class);
        intent.putExtra(DetailActivity.JOKE_STRING,output);
        startActivity(intent);
    }

    @Override
    public void onResume() {
        super.onResume();

    }
}
